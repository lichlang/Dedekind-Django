from sua.models import Nonce
import time


EXPIRE_TIME = 120


def cleanNonce():
        cleanNonces = Nonce.objects.filter(timestamp__lte=int(time.time())-EXPIRE_TIME)
        cleanedNonceIDs = []
        for nonce in cleanNonces:
            cleanedNonceIDs.append(nonce.pk)
            nonce.delete()
        self.stdout.write('删除了%s个Nonce' % len(cleanedNonceIDs))
