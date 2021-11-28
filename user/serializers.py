class MultiUserSerializer:

    @staticmethod
    def serializer(users, page_size, page):
        return {
            "results": [UserSerializer.serializer(user) for user in users],
            "page": int(page),
            "page_size": int(page_size),
        }


class UserSerializer:
    @staticmethod
    def serializer(user):
        return {
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "image": str(user.image),
                "resized_image": str(user.resized_image),
                "gender": user.gender,
                "description_text": user.description_text,
                "location": user.location,
                "timestamp": str(user.timestamp),
            }