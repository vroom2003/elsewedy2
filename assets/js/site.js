(function () {
  const year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();

  const header = document.querySelector(".header");
  const toggle = document.querySelector(".menu-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", () => header.classList.toggle("is-open"));
  }

  document.querySelectorAll(".nav > li > a").forEach((link) => {
    if (!link.querySelector(".caret")) return;
    link.addEventListener("click", (event) => {
      if (window.innerWidth > 960) return;
      event.preventDefault();
      link.parentElement.classList.toggle("is-open");
    });
  });

  document.querySelectorAll("form[data-demo-form]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const notice = form.parentElement.querySelector(".notice");
      form.reset();
      if (notice) notice.classList.add("show");
    });
  });

  const toTop = document.querySelector(".to-top");
  if (toTop) {
    toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  const params = new URLSearchParams(window.location.search);
  const q = params.get("q");
  const qOut = document.querySelector("[data-query]");
  if (q && qOut) qOut.textContent = q;
})();
