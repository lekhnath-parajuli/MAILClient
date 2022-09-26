#!.env/bin/python

from imapclient import IMAPClient
from sqlalchemy.orm import Session
from auth.config import config
from model import Email, engine
from imap_client import (
    get_message_ids,
    all_folders,
    sync_with_remote,
    delete_from_local,
)


with IMAPClient(config.IMAP_SERVER) as server, Session(bind=engine) as session:
    server.login(username=config.USERNAME, password=config.PASSWORD)
    all_folders = all_folders(server)
    local_mails = session.query(Email).all()

    for folder in all_folders:
        remote_mail_uids = set(get_message_ids(server, folder))
        local_mail_uids = {mail.message_uid for mail in local_mails
                           if mail.folder_name == folder}

        not_in_local = remote_mail_uids - local_mail_uids
        not_in_remote = local_mail_uids - remote_mail_uids
        if not_in_local:
            sync_with_remote(session, Email, not_in_local, folder)
        if not_in_remote:
            delete_from_local(session, Email, not_in_remote, folder)
    session.commit()
