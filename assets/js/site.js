(function () {
  // Update year elements
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear().toString();
  });

  // Mobile menu toggle
  const header = document.querySelector(".header");
  const menuBtn = document.querySelector(".menu-toggle");
  if (header && menuBtn) {
    menuBtn.addEventListener("click", () => {
      header.classList.toggle("is-open");
    });
  }

  // Mobile submenu toggles
  document.querySelectorAll(".nav > li").forEach((li) => {
    const link = li.querySelector(":scope > a");
    const submenu = li.querySelector(".submenu");
    if (link && submenu) {
      link.addEventListener("click", (e) => {
        if (window.innerWidth <= 960) {
          e.preventDefault();
          li.classList.toggle("is-open");
        }
      });
    }
  });

  // Form handling
  document.querySelectorAll("form[data-demo-form]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const notice = form.querySelector(".notice");
      if (notice) {
        notice.classList.add("show");
        form.reset();
      }
    });
  });

  // Back to top
  const toTop = document.querySelector(".to-top");
  if (toTop) {
    toTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Search query display
  const queryEl = document.querySelector("[data-query]");
  if (queryEl) {
    const params = new URLSearchParams(window.location.search);
    const q = params.get("q");
    if (q) {
      queryEl.textContent = `"${q}"`;
    }
  }
})();
