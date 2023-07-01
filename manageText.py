import hashlib


def manageText(text_body, filee, flag_commentsPosts, post_content=None):
    if flag_commentsPosts == True:
        # manage a COMMENT
        hash_v = text_body.encode()
        hash_v = hashlib.sha256(hash_v).hexdigest()
        text_body = "- **COMMENT**: \n\n" + text_body + "\n\n"
        filee.write(text_body)
        hash_v_body = "    - **HASHED COMMENT**: \n\n" + hash_v + "\n\n"
        filee.write(hash_v_body)
        return hash_v
    else:
        # manage a POST
        hash_v = text_body.encode()
        hash_v = hashlib.sha256(hash_v).hexdigest()
        text_body = "- **POST TITLE**: \n\n" + text_body + "\n\n"
        filee.write(text_body)
        text_body = "- **POST BODY**: \n\n" + post_content + "\n\n"
        filee.write(text_body)
        hash_v_body = "    - **HASHED BODY**: \n\n" + hash_v + "\n\n"
        filee.write(hash_v_body)
        return hash_v
