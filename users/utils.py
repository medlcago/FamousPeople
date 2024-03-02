def get_avatar_upload_path(instance, filename):
    base_path = "avatars"
    return f"{base_path}/{instance.user.username}/{filename}"
