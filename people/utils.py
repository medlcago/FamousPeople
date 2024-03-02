def get_photo_upload_path(instance, filename):
    base_path = "photos"
    return f"{base_path}/{instance.slug}/{filename}"
