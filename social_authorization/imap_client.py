from imapclient import IMAPClient
import email
from sqlalchemy import and_


def get_messages(server: IMAPClient, folder: str, message_ids: list):
    messages = {}
    if not message_ids:
        return messages
    server.select_folder(folder, readonly=True)
    for uid, message_data in server.fetch([], "RFC822").items():
        email_message = email.message_from_bytes(message_data[b"RFC822"])
        messages[uid] = email_message
    return messages


def sync_with_remote(session, model, message_uids, folder):
    new_messages = []
    for uid in message_uids:
        new_messages.append(
            model(
                message_uid=uid,
                folder_name=folder,
            ))
    session.add_all(new_messages)


def delete_from_local(session, model, message_uids, folder):
    for uid in message_uids:
        session.query(model).filter(
            and_(
                model.message_uid == uid,
                model.folder_name == folder,
            )).delete()


def get_message_ids(server: IMAPClient, folder: str):
    try:
        server.select_folder(folder, readonly=True)
        return server.search(criteria='ALL', charset=None)
    except Exception as e:
        print(f'Exception while fetching  {folder} data\n [x] {e}')
        return []


def all_folders(server: IMAPClient):
    return [folder for _, _, folder in server.list_folders()]


def create_folder(server: IMAPClient, folder: str):
    server.create_folder(folder)


def create_sub_folder(server: IMAPClient, parent: str, child: str):
    server.select_folder(parent)
    server.create_folder(child)


def delete_folder(server: IMAPClient, folder: str):
    server.delete_folder(folder)


def delete_sub_folder(server: IMAPClient, parent: str, child: str):
    server.select_folder(parent)
    server.delete_folder(child)


def delete_message(server: IMAPClient, folder: str, message_ids: list[int]):
    server.select_folder(folder)
    server.delete_messages(message_ids)
