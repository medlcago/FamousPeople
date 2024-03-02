def get_photo_upload_path(instance, filename):
    base_path = "photos"
    return f"{base_path}/{instance.slug}/{filename}"


def get_avatar_upload_path(instance, filename):
    base_path = "avatars"
    return f"{base_path}/{instance.user.username}/{filename}"
