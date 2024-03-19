import uuid
from app.liberary.db.session import with_session
from app.liberary.db.models.file_model import FileModel



@with_session
def add_file_to_db(session, user_id, file_path, file_type) -> str:
    """
    新增上传文件
    """

    file_id = uuid.uuid4().hex
    file_obj = FileModel(file_id=file_id, user_id=user_id, file_path=file_path, file_type=file_type,
                                 delete_tag=0)

    session.add(file_obj)
    session.commit()
    return file_obj.file_id
