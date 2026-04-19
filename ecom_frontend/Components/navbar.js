class MaisonNavbar extends HTMLElement {
  connectedCallback() {
    const active = this.getAttribute("active") || "";

    this.innerHTML = `
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Jost:wght@300;400;500&display=swap');
  
          maison-navbar *,
          maison-navbar *::before,
          maison-navbar *::after { box-sizing: border-box; margin: 0; padding: 0; }
  
          maison-navbar {
            display: block;
            position: sticky;
            top: 0;
            z-index: 100;
          }
  
          .mn-nav {
            background: var(--cream, #faf7f2);
            border-bottom: 1px solid var(--border, #ddd3c2);
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            padding: 0 48px;
            height: 68px;
          }
  
          .mn-left { display: flex; align-items: center; gap: 10px; }
  
          .mn-avatar {
            width: 34px; height: 34px; border-radius: 50%;
            background: var(--bark, #7a6248);
            display: flex; align-items: center; justify-content: center;
            font-family: "Cormorant Garamond", serif;
            font-size: 15px; color: var(--cream, #faf7f2);
            font-weight: 600; flex-shrink: 0;
          }
          .mn-user-name { font-size: 13px; color: var(--text, #2c231a); letter-spacing: 0.3px; font-family: "Jost", sans-serif; }
          .mn-user-email { font-size: 11px; color: var(--muted, #9a8878); letter-spacing: 0.5px; text-transform: uppercase; font-family: "Jost", sans-serif; }
  
          .mn-logo {
            text-align: center;
            font-family: "Cormorant Garamond", serif;
            font-size: 30px; font-weight: 600;
            letter-spacing: 6px; text-transform: uppercase;
            color: var(--ink, #1e1810);
            text-decoration: none;
          }
  
          .mn-right { display: flex; gap: 16px; align-items: center; justify-content: flex-end; }
  
          .mn-link {
            color: var(--muted, #9a8878); text-decoration: none;
            font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase;
            transition: color 0.2s; font-family: "Jost", sans-serif;
            font-weight: 300; background: none; border: none; cursor: pointer;
            position: relative; padding-bottom: 2px;
          }
          .mn-link:hover { color: var(--ink, #1e1810); }
          .mn-link.mn-active { color: var(--ink, #1e1810); }
          .mn-link.mn-active::after {
            content: '';
            position: absolute; bottom: -2px; left: 0; right: 0;
            height: 1px; background: var(--ink, #1e1810);
          }
  
          .mn-logout {
            background: none; border: 1px solid var(--border, #ddd3c2);
            color: var(--muted, #9a8878); padding: 7px 18px; border-radius: 2px;
            font-family: "Jost", sans-serif; font-size: 11px;
            letter-spacing: 1.5px; text-transform: uppercase;
            cursor: pointer; transition: all 0.2s;
          }
          .mn-logout:hover { border-color: #c0392b; color: #c0392b; }
  
          @media (max-width: 768px) {
            .mn-nav { padding: 0 20px; }
            .mn-user-email { display: none; }
          }
        </style>
  
        <nav class="mn-nav">
          <div class="mn-left">
            <div class="mn-avatar" id="mn-avatar">…</div>
            <div>
              <div class="mn-user-name" id="mn-username">…</div>
              <div class="mn-user-email" id="mn-email"></div>
            </div>
          </div>
  
          <a href="/Dashboard/dashboard.html" class="mn-logo">Maison</a>
  
          <div class="mn-right">
            <a href="/ecom_frontend/Dashboard/dashboard.html" class="mn-link ${
              active === "shop" ? "mn-active" : ""
            }">Shop</a>
            <a href="/ecom_frontend/Cart/cart.html"           class="mn-link ${
              active === "cart" ? "mn-active" : ""
            }">Bag</a>
            <a href="/ecom_frontend/Orders/orders.html"       class="mn-link ${
              active === "orders" ? "mn-active" : ""
            }">Orders</a>
            <button class="mn-logout" id="mn-logout">Logout</button>
          </div>
        </nav>
      `;

    this._loadUser();
    this.querySelector("#mn-logout").addEventListener("click", () => {
      localStorage.removeItem("accessToken");
      location.href = "/ecom_frontend/Login/login.html";
    });
  }

  _loadUser() {
    const token = localStorage.getItem("accessToken");
    if (!token) return;
    fetch("http://localhost:8000/api/users/me/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (!data) return;
        const name = data.first_name || data.username || "User";
        this.querySelector("#mn-avatar").textContent = name
          .slice(0, 2)
          .toUpperCase();
        this.querySelector("#mn-username").textContent = name;
        if (data.email)
          this.querySelector("#mn-email").textContent = data.email;
      })
      .catch(() => {});
  }
}

customElements.define("maison-navbar", MaisonNavbar);
