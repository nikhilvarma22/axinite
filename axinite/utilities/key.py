import uuid

#----------------------------------------------------------------------------
def get_verification_key():
    """
    This method is used to return a random uuid key, which is then used in 
    verifying.
    """
    return uuid.uuid4().__str__()
#----------------------------------------------------------------------------

