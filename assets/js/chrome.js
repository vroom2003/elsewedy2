(function () {
  const r = document.body.getAttribute("data-root") || "";

  const header = `
<div class="topbar">
  <div class="wrap">
    <a href="${r}clients.html">Our Clients</a>
    <a href="${r}locations.html">Our Locations</a>
    <a href="${r}contact.html">Contact</a>
    <a href="${r}jobs.html">Jobs</a>
    <a href="${r}news.html">News</a>
    <a href="${r}send-cv.html">Send your CV</a>
  </div>
</div>
<header class="header">
  <div class="wrap header-row">
    <a class="logo" href="${r}index.html">
      <img src="${r}assets/img/logo.svg" alt="" width="42" height="42">
      <div>
        <strong>ELSEWEDY</strong>
        <span>People &amp; Talent</span>
      </div>
    </a>
    <button class="menu-toggle" type="button" aria-label="Open menu">☰</button>
    <ul class="nav">
      <li>
        <a href="${r}executive-search.html">Executive Recruitment <i class="caret"></i></a>
        <div class="submenu">
          <a href="${r}executive-search.html">Executive Search</a>
          <a href="${r}candidate-profiles.html">Candidate Profiles</a>
          <a href="${r}psychometric.html">Psychometric Testing</a>
          <a href="${r}placement.html">Placement Services</a>
        </div>
      </li>
      <li>
        <a href="${r}hr-consulting.html">Human Resources Solutions <i class="caret"></i></a>
        <div class="submenu">
          <a href="${r}hr-systems.html">HR Systems</a>
          <a href="${r}hr-consulting.html">HR Consulting</a>
          <a href="${r}salary-surveys.html">Salary &amp; Benefits Surveys</a>
        </div>
      </li>
      <li>
        <a href="${r}outsourcing.html">HR Services <i class="caret"></i></a>
        <div class="submenu">
          <a href="${r}outsourcing.html">Outsourcing</a>
          <a href="${r}payroll.html">Payroll Outsourcing</a>
          <a href="${r}employer-of-record.html">Employer of Record</a>
          <a href="${r}labour-law.html">Zimbabwe Labour Law Consulting</a>
          <a href="${r}government-affairs.html">Governmental Affairs Solutions</a>
          <a href="${r}talent-management.html">Talent Management</a>
          <a href="${r}employer-branding.html">Employment Branding</a>
          <a href="${r}employment-outsourcing.html">Global Employment Outsourcing</a>
        </div>
      </li>
      <li>
        <a href="${r}global-staffing.html">Global Staffing <i class="caret"></i></a>
        <div class="submenu">
          <a href="${r}work-permits.html">Work Permit &amp; Visas for Expats</a>
          <a href="${r}attestation.html">Attestation Services</a>
        </div>
      </li>
      <li><a href="${r}jobs.html">Vacancies</a></li>
    </ul>
    <form class="search" action="${r}search.html" method="get">
      <input type="search" name="q" placeholder="Search" aria-label="Search">
      <button type="submit" aria-label="Submit search">⌕</button>
    </form>
  </div>
</header>`;

  const footer = `
<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <h4>Elsewedy People &amp; Talent</h4>
      <p>Professional consulting in internal audit, final accounts, job appraisals, training &amp; development, and labour outsourcing across Zimbabwe. Registered under Conrad Forester Investments (Reg No: 260/2021).</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="${r}executive-search.html">Executive Search</a></li>
        <li><a href="${r}outsourcing.html">Labour Outsourcing</a></li>
        <li><a href="${r}payroll.html">Payroll Services</a></li>
        <li><a href="${r}hr-consulting.html">HR &amp; Internal Audit</a></li>
      </ul>
    </div>
    <div>
      <h4>For candidates</h4>
      <ul>
        <li><a href="${r}jobs.html">Open vacancies</a></li>
        <li><a href="${r}send-cv.html">Send your CV</a></li>
        <li><a href="${r}candidate-profiles.html">Talent community</a></li>
        <li><a href="${r}news.html">News &amp; Insights</a></li>
      </ul>
    </div>
    <div>
      <h4>Offices</h4>
      <ul>
        <li>Harare</li>
        <li>Bulawayo</li>
        <li>Mutare</li>
        <li><a href="${r}contact.html">Contact the desk</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>© <span data-year></span> Elsewedy People &amp; Talent · Conrad Forester Investments (Reg No: 260/2021). All rights reserved.</span>
    <span>
      <a href="${r}privacy.html">Privacy Policy</a>
      ·
      <a href="${r}cookies.html">Cookie Policy</a>
      ·
      <a href="${r}contact.html">Contact Us</a>
    </span>
  </div>
</footer>
<button class="to-top" type="button" aria-label="Back to top">↑</button>`;

  document.querySelectorAll("[data-include='header']").forEach((el) => {
    el.outerHTML = header;
  });
  document.querySelectorAll("[data-include='footer']").forEach((el) => {
    el.outerHTML = footer;
  });
})();
