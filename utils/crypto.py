import json
import qrcode
from config import CRYPTO_WALLETS

def generate_payment_qr(wallet_address: str, amount: float):
    payment_url = f"{wallet_address}?amount={amount}"
    img = qrcode.make(payment_url)
    img_path = f"{wallet_address}.png"
    img.save(img_path)
    return img_path

def get_wallets():
    return json.loads(CRYPTO_WALLETS)
