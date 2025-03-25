import hashlib

def hashPost(filee, postTitle, postContent):
    hash_v = postTitle.encode()
    hash_v = hashlib.sha256(hash_v).hexdigest()
    text_body = "- **POST TITLE**: \n\n" + postTitle + "\n\n"
    filee.write(text_body)
    text_body = "- **POST BODY**: \n\n" + postContent + "\n\n"
    filee.write(text_body)
    hash_v_body = "    - **HASHED BODY**: \n\n" + hash_v + "\n\n"
    filee.write(hash_v_body)
    return hash_v
    

def hashComment(filee, commentBody):
    hash_v = commentBody.encode()
    hash_v = hashlib.sha256(hash_v).hexdigest()
    text_body = "- **COMMENT**: \n\n" + commentBody + "\n\n"
    filee.write(text_body)
    hash_v_body = "    - **HASHED COMMENT**: \n\n" + hash_v + "\n\n"
    filee.write(hash_v_body)
    return hash_v
