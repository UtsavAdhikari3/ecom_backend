const BASE_URL = "https://apiecom.adhikariutsav.com.np";
const WALLET_URL = "https://apiwallet.adhikariutsav.com.np";

const API = {
  LOGIN: BASE_URL + "/api/users/login/",
  REGISTER: BASE_URL + "/api/users/register/",
  ME: BASE_URL + "/api/users/me/",
  PRODUCT: BASE_URL + "/api/products/",
  CART_COUNT: BASE_URL + "/api/cart/items/",

  PAYMENT_CONFIRM: WALLET_URL + "/api/payment/confirm_payment/",
  TRANSFER_MERCHANT: WALLET_URL + "/api/wallet/transfer_merchant/",
};
