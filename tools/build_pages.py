from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def chrome(root: str, title: str, active: str = "") -> tuple[str, str]:
    r = root
    header = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{r}assets/css/main.css">
  <link rel="icon" href="{r}assets/img/logo.svg">
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <div class="wrap">
    <a href="{r}clients.html">Our Clients</a>
    <a href="{r}locations.html">Our Locations</a>
    <a href="{r}contact.html">Contact</a>
    <a href="{r}jobs.html">Jobs</a>
    <a href="{r}news.html">News</a>
    <a href="{r}send-cv.html">Send your CV</a>
  </div>
</div>
<header class="header">
  <div class="wrap header-row">
    <a class="logo" href="{r}index.html">
      <img src="{r}assets/img/logo.svg" alt="" width="42" height="42">
      <div>
        <strong>ELSEWEDY</strong>
        <span>People &amp; Talent</span>
      </div>
    </a>
    <button class="menu-toggle" type="button" aria-label="Open menu">☰</button>
    <ul class="nav">
      <li>
        <a href="{r}executive-search.html">Executive Recruitment <i class="caret"></i></a>
        <div class="submenu">
          <a href="{r}executive-search.html">Executive Search</a>
          <a href="{r}candidate-profiles.html">Candidate Profiles</a>
          <a href="{r}psychometric.html">Psychometric Testing</a>
          <a href="{r}placement.html">Placement Services</a>
        </div>
      </li>
      <li>
        <a href="{r}hr-consulting.html">Human Resources Solutions <i class="caret"></i></a>
        <div class="submenu">
          <a href="{r}hr-systems.html">HR Systems</a>
          <a href="{r}hr-consulting.html">HR &amp; Internal Audit Consulting</a>
          <a href="{r}salary-surveys.html">Salary &amp; Benefits Surveys</a>
        </div>
      </li>
      <li>
        <a href="{r}outsourcing.html">HR Services <i class="caret"></i></a>
        <div class="submenu">
          <a href="{r}outsourcing.html">Labour Outsourcing</a>
          <a href="{r}payroll.html">Payroll Outsourcing</a>
          <a href="{r}employer-of-record.html">Employer of Record</a>
          <a href="{r}labour-law.html">Zimbabwe Labour Law Consulting</a>
          <a href="{r}government-affairs.html">Governmental Affairs Solutions</a>
          <a href="{r}talent-management.html">Talent Management &amp; Training</a>
          <a href="{r}employer-branding.html">Employment Branding</a>
          <a href="{r}employment-outsourcing.html">Global Employment Outsourcing</a>
        </div>
      </li>
      <li>
        <a href="{r}global-staffing.html">Global Staffing <i class="caret"></i></a>
        <div class="submenu">
          <a href="{r}work-permits.html">Work Permit &amp; Visas for Expats</a>
          <a href="{r}attestation.html">Attestation Services</a>
        </div>
      </li>
      <li><a href="{r}jobs.html">Vacancies</a></li>
    </ul>
    <form class="search" action="{r}search.html" method="get">
      <input type="search" name="q" placeholder="Search" aria-label="Search">
      <button type="submit" aria-label="Submit search">⌕</button>
    </form>
  </div>
</header>
<main id="main">
"""
    footer = f"""
</main>
<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <h4>Elsewedy People &amp; Talent</h4>
      <p>Professional consulting firm specializing in internal audit, preparation of final accounts, job appraisals, training &amp; development, and labour outsourcing across Zimbabwe. Registered under Conrad Forester Investments (Reg No: 260/2021).</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="{r}executive-search.html">Executive Search</a></li>
        <li><a href="{r}outsourcing.html">Labour Outsourcing</a></li>
        <li><a href="{r}payroll.html">Payroll Services</a></li>
        <li><a href="{r}hr-consulting.html">Internal Audit &amp; HR</a></li>
      </ul>
    </div>
    <div>
      <h4>For candidates</h4>
      <ul>
        <li><a href="{r}jobs.html">Open vacancies</a></li>
        <li><a href="{r}send-cv.html">Send your CV</a></li>
        <li><a href="{r}candidate-profiles.html">Talent community</a></li>
        <li><a href="{r}news.html">News &amp; Insights</a></li>
      </ul>
    </div>
    <div>
      <h4>Offices</h4>
      <ul>
        <li>Harare (Head Office)</li>
        <li>Bulawayo</li>
        <li>Mutare</li>
        <li><a href="{r}contact.html">Contact the desk</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>© <span data-year></span> Elsewedy People &amp; Talent · Conrad Forester Investments (Reg No: 260/2021). All rights reserved.</span>
    <span>
      <a href="{r}privacy.html">Privacy Policy</a>
      ·
      <a href="{r}cookies.html">Cookie Policy</a>
      ·
      <a href="{r}contact.html">Contact Us</a>
    </span>
  </div>
</footer>
<button class="to-top" type="button" aria-label="Back to top">↑</button>
<script src="{r}assets/js/site.js"></script>
</body>
</html>
"""
    return header, footer


def page(path: str, title: str, body: str, nested: bool = False) -> None:
    root = "../" if nested else ""
    header, footer = chrome(root, title)
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + body + footer, encoding="utf-8")


pages = {}

pages["index.html"] = (
    "People & Talent | Elsewedy Zimbabwe",
    """
<section class="hero">
  <div class="wrap hero-inner">
    <p class="eyebrow">Internal Audit &amp; Talent Partner in Zimbabwe</p>
    <h1>Strong operations<br>built on strong<br>internal audit.</h1>
    <a class="btn" href="outsourcing.html">Explore workforce &amp; audit solutions</a>
  </div>
</section>
<section class="section">
  <div class="wrap center">
    <p class="muted">Enterprises and sectors we serve across Zimbabwe</p>
    <div class="clients">
      <div class="client-mark">ZIMBABWE POWER</div>
      <div class="client-mark">ZIMPLATS LOGISTICS</div>
      <div class="client-mark">HARARE INDUSTRIAL</div>
      <div class="client-mark">BULAWAYO METALS</div>
      <div class="client-mark">MUTARE AGRO</div>
      <div class="client-mark">GWERU MINING</div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div>
      <p class="kicker">Professional Consulting Firm</p>
      <h2>Integrity. Insight. Impact.</h2>
      <p class="lead">Elsewedy People &amp; Talent (operating under Conrad Forester Investments, Reg No: 260/2021) delivers quality solutions that help organizations improve operational efficiency, strengthen governance, ensure compliance, and develop their workforce across Zimbabwe.</p>
      <div class="cards-2">
        <article class="card">
          <h3>Internal Audit &amp; Final Accounts</h3>
          <p>Risk assessment, preparation of final accounts, governance frameworks, and internal controls for schools, commercial entities, and corporate groups.</p>
          <a href="hr-consulting.html">Learn more</a>
        </article>
        <article class="card">
          <h3>Labour Outsourcing &amp; Training</h3>
          <p>Compliant workforce outsourcing, job appraisals, staff training &amp; development, and technical recruitment across Harare, Bulawayo, and regional hubs.</p>
          <a href="outsourcing.html">Learn more</a>
        </article>
      </div>
    </div>
    <div class="photo" style="background-image:linear-gradient(rgba(15,37,55,.2),rgba(15,37,55,.2)), url('assets/img/hero.svg')">
      <span class="badge-circle"></span>
    </div>
  </div>
</section>
<section class="section panel">
  <div class="wrap stats">
    <div>
      <p class="kicker" style="color:#a1d855">Our Services</p>
      <div class="stat-num">260/2021</div>
      <p style="margin-top:12px; color:#c0c9d4">Registration Number under Conrad Forester Investments. Operating t/a Elsewedy People &amp; Talent.</p>
    </div>
    <div class="pillars">
      <div class="pillar">
        <div class="icon-box">01</div>
        <div>
          <strong>Internal Audit Functions &amp; Final Accounts</strong>
          <div class="muted">Independent objective assurance, governance, preparation of final accounts, and risk assessment.</div>
        </div>
        <a href="hr-consulting.html">Audit Solutions</a>
      </div>
      <div class="pillar">
        <div class="icon-box">02</div>
        <div>
          <strong>Job Appraisals &amp; Training</strong>
          <div class="muted">Capacity building, workforce appraisal systems, and professional staff development.</div>
        </div>
        <a href="talent-management.html">Training &amp; Development</a>
      </div>
      <div class="pillar">
        <div class="icon-box">03</div>
        <div>
          <strong>Labour Outsourcing &amp; Payroll</strong>
          <div class="muted">Compliant employment management under Zimbabwean Labour Act regulations.</div>
        </div>
        <a href="outsourcing.html">Labour Outsourcing</a>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="jobs-head">
      <div>
        <p class="kicker">Careers</p>
        <h2>Current Opportunities in Zimbabwe</h2>
        <p class="muted">Submit your profile to connect with our talent community and upcoming corporate placements.</p>
      </div>
      <a class="btn" href="send-cv.html">Upload your CV</a>
    </div>
    <div class="job-grid">
      <article class="job-card">
        <span class="tag">Human Resources</span>
        <h3><a href="jobs/plant-hr-bp.html">Plant HR &amp; Operations Lead</a></h3>
        <p>Lead employee relations, job appraisals, and shop-floor HR operations for a manufacturing plant in Harare.</p>
        <a href="jobs/plant-hr-bp.html">Read role description</a>
      </article>
      <article class="job-card">
        <span class="tag">Internal Audit</span>
        <h3><a href="jobs/shift-operations-lead.html">Internal Audit &amp; Compliance Officer</a></h3>
        <p>Conduct financial audits, internal control reviews, and risk assessment for commercial clients in Bulawayo.</p>
        <a href="jobs/shift-operations-lead.html">Read role description</a>
      </article>
    </div>
  </div>
</section>
<section class="section" style="background:var(--paper)">
  <div class="wrap split">
    <div>
      <p class="kicker">Contact Us</p>
      <h2>Your trusted partner in operational excellence.</h2>
      <p>Whether you require internal audit functions, final accounts preparation, job appraisals, or workforce outsourcing in Zimbabwe, our desk is ready to assist.</p>
      <p style="margin-top:16px"><strong>Contact Person:</strong> Mavhondo Fanwell Tatenda<br><strong>Contact Number:</strong> +263 713 174 032<br><strong>Email:</strong> info@elsewedyconsultancy.com</p>
      <a class="btn" href="contact.html" style="margin-top:12px">Talk to our consultants</a>
    </div>
    <form class="form card" data-demo-form>
      <h3>Request a Consultation</h3>
      <input name="name" placeholder="Name*" required>
      <input name="company" placeholder="Company / Organization*" required>
      <input name="phone" placeholder="Phone Number*" required>
      <input type="email" name="email" placeholder="Email Address*" required>
      <textarea name="message" placeholder="How can we assist you with Internal Audit, Accounts, or Outsourcing?*" required></textarea>
      <button class="btn" type="submit">Submit Request</button>
      <p class="notice">Thank you for your request. Our team will contact you shortly.</p>
    </form>
  </div>
</section>
""",
    False,
)

SERVICE_PAGES = {
    "executive-search.html": (
        "Executive Search | Elsewedy Zimbabwe",
        "Executive Search",
        "We map leadership benches for manufacturing, mining, finance, educational institutions, and corporate groups across Zimbabwe. Searches stay confidential, criteria are aligned with board requirements, and shortlists feature proven track records.",
        [
            "C-suite, plant directors, internal audit leads, and operational heads",
            "Finance controllers, HR directors, and risk management executives",
            "Confidential replacements and specialized country manager roles",
            "Structured 90-day onboarding support for senior placements",
        ],
    ),
    "candidate-profiles.html": (
        "Candidate Profiles | Elsewedy Zimbabwe",
        "Candidate Profiles",
        "Assessed talent files for internal auditors, accounting professionals, HR managers, engineers, and technical supervisors experienced in Zimbabwean industries.",
        [
            "Pre-screened financial, audit, and technical specialists",
            "Competency ratings from structured executive interviews",
            "Consent-based matching for confidential openings",
            "Updated quarterly talent benchmarking",
        ],
    ),
    "psychometric.html": (
        "Psychometric Testing | Elsewedy Zimbabwe",
        "Psychometric Testing",
        "Ability and work-style assessments used as objective evaluation alongside interviews and practical technical trials for key staff appointments.",
        [
            "Numerical and analytical reasoning screens for accounting & audit positions",
            "Leadership style and decision-making evaluations",
            "Customized assessments for supervisory and management tiers",
            "Clear diagnostic reports for selection panels",
        ],
    ),
    "placement.html": (
        "Placement Services | Elsewedy Zimbabwe",
        "Placement Services",
        "End-to-end placement for mid-level professional, accounting, administrative, and technician roles across Harare, Bulawayo, Mutare, and Gweru.",
        [
            "Role scorecards defined with department managers",
            "Market mapping across Zimbabwean industrial corridors",
            "Compensation alignment against current market pay data",
            "Structured follow-up during probationary periods",
        ],
    ),
    "hr-systems.html": (
        "HR Systems & Payroll | Elsewedy Zimbabwe",
        "HR Systems & Payroll",
        "Practical support selecting, configuring, and maintaining HRIS and payroll data to ensure full alignment with Zimbabwean statutory obligations.",
        [
            "HR process engineering prior to software deployment",
            "Employee master data cleanup and organizational structures",
            "Self-service portal configuration for managers and staff",
            "Reporting tools for executive management and auditors",
        ],
    ),
    "hr-consulting.html": (
        "Internal Audit & HR Consulting | Elsewedy Zimbabwe",
        "Internal Audit & HR Consulting",
        "Integrated consulting services covering internal audit functions, governance frameworks, risk assessment, preparation of final accounts, and HR policy development.",
        [
            "Internal audit functions & internal control evaluations",
            "Preparation of final accounts & statutory financial review",
            "Risk assessment & governance framework development",
            "Job architecture, grading, and organizational restructuring",
        ],
    ),
    "salary-surveys.html": (
        "Salary & Benefits Surveys | Elsewedy Zimbabwe",
        "Salary & Benefits Surveys",
        "Confidential compensation snapshots across mining, manufacturing, commercial, and educational sectors in Zimbabwe.",
        [
            "Role matching to standardized industry benchmarking catalogues",
            "Base salary, hardship allowances, and performance incentives",
            "Sector-specific shift and site location premiums",
            "Executive-level board reporting packs",
        ],
    ),
    "outsourcing.html": (
        "Labour Outsourcing | Elsewedy Zimbabwe",
        "Labour Outsourcing",
        "We employ assigned personnel, manage employment contracts, process payroll, and coordinate on-site HR administration while you retain operational direction.",
        [
            "Employment contract administration compliant with Zimbabwean Labour Law",
            "NSSA, medical aid, and statutory insurance compliance",
            "Dedicated on-site HR supervision for large deployments",
            "Clear exit management and handover procedures",
        ],
    ),
    "payroll.html": (
        "Payroll Outsourcing | Elsewedy Zimbabwe",
        "Payroll Outsourcing",
        "Full monthly payroll calculation, PAYE tax filing, NSSA statutory contributions, and secure payslip delivery across Zimbabwe.",
        [
            "Time & attendance reconciliation to net pay calculation",
            "ZIMRA tax and NSSA statutory return compliance",
            "Automated electronic bank payment files",
            "Complete audit trail for internal and external financial reviews",
        ],
    ),
    "employer-of-record.html": (
        "Employer of Record | Elsewedy Zimbabwe",
        "Employer of Record",
        "A fully compliant Zimbabwean Employer of Record (EOR) service allowing international companies to deploy specialist talent in Zimbabwe without establishing a local legal entity.",
        [
            "Local statutory employment contract management",
            "Payroll, tax withholding, and benefit administration",
            "Workplace policy alignment and local legal compliance",
            "Seamless transition options should you set up a direct local branch",
        ],
    ),
    "labour-law.html": (
        "Zimbabwe Labour Law Consulting | Elsewedy Zimbabwe",
        "Zimbabwe Labour Law Consulting",
        "Expert advisory on the Zimbabwean Labour Act [Chapter 28:01], employment contracts, workplace discipline, retrenchment codes, and dispute resolution.",
        [
            "Standardized employment templates for all worker classifications",
            "Disciplinary hearing guidance and code of conduct alignment",
            "Labour officer & conciliation representation support",
            "Regular updates when statutory labour frameworks change",
        ],
    ),
    "government-affairs.html": (
        "Governmental Affairs | Elsewedy Zimbabwe",
        "Governmental Affairs",
        "Coordination of statutory registration, Ministry of Labour filings, NSSA, and regulatory compliance requirements in Zimbabwe.",
        [
            "Workplace registration and statutory filings",
            "NSSA and Ministry inspectorate audit preparations",
            "Licensing & regulatory tracking with assigned consultants",
            "Expat work permit and immigration file coordination",
        ],
    ),
    "talent-management.html": (
        "Talent Management & Training | Elsewedy Zimbabwe",
        "Talent Management & Training",
        "Capacity building, job appraisals, performance management systems, and workforce training & development designed to empower your staff.",
        [
            "Structured job appraisal systems and performance KPIs",
            "Capacity building and professional skill training sprints",
            "Critical-role succession mapping for industrial and school leadership",
            "Graduate and technician development programmes",
        ],
    ),
    "employer-branding.html": (
        "Employment Branding | Elsewedy Zimbabwe",
        "Employment Branding",
        "Helping Zimbabwean organizations define and communicate their unique employer value proposition to attract top-tier talent.",
        [
            "Workplace culture and employer brand messaging",
            "Interview toolkits for hiring panels",
            "Graduate recruitment and university liaison strategies",
            "Onboarding experience optimization",
        ],
    ),
    "employment-outsourcing.html": (
        "Global Employment Outsourcing | Elsewedy Zimbabwe",
        "Global Employment Outsourcing",
        "Cross-border employment support for regional infrastructure, energy, and commercial projects in Zimbabwe and neighboring SADC countries.",
        [
            "Multi-country onboarding and compliance checklists",
            "Cross-border currency and compensation management",
            "Regional partner coordination under a central project lead",
            "Consolidated management reporting packs",
        ],
    ),
    "global-staffing.html": (
        "Global Staffing | Elsewedy Zimbabwe",
        "Global Staffing",
        "Project and rotational staffing solutions for mining, energy, agriculture, and construction programs requiring specialist mobility.",
        [
            "Technical specialist and engineering rosters",
            "Mobilization and logistics management",
            "Site safety briefings and compliance protocols",
            "Demobilization and project handover management",
        ],
    ),
    "work-permits.html": (
        "Work Permits & Visas | Elsewedy Zimbabwe",
        "Work Permits & Visas",
        "Document preparation, submission, and tracking for expatriate specialists requiring lawful work and residency permits in Zimbabwe.",
        [
            "Immigration document checklists by nationality and skill set",
            "Department of Immigration file tracking",
            "Spouse and dependent residence permit coordination",
            "Permit renewal calendars and compliance monitoring",
        ],
    ),
    "attestation.html": (
        "Attestation Services | Elsewedy Zimbabwe",
        "Attestation Services",
        "Comprehensive document authentication, degree attestation, police clearances, and corporate notarization services for employment compliance.",
        [
            "Educational degree & professional diploma verification",
            "Corporate legal document authentication",
            "Official translation and consular endorsement coordination",
            "Regular progress updates through to final delivery",
        ],
    ),
}


def service_body(heading: str, intro: str, items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Service Solution</p>
    <h1>{heading}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Key Features &amp; Deliverables</h2>
      <ul class="list-check">{lis}</ul>
      <p style="margin-top:28px"><a class="btn" href="contact.html">Request a Consultation</a></p>
    </div>
    <aside class="card">
      <h3>Who We Serve</h3>
      <p>Schools, mining enterprises, industrial manufacturers, commercial groups, and corporate boards seeking reliable internal audit and workforce solutions across Zimbabwe.</p>
      <p class="muted" style="margin-top:16px; border-top: 1px solid var(--line); padding-top:12px;"><strong>Entity:</strong> Conrad Forester Investments (Reg No: 260/2021)<br><strong>Contact:</strong> Mavhondo Fanwell Tatenda (+263 713 174 032)</p>
    </aside>
  </div>
</section>
"""


for filename, (title, heading, intro, items) in SERVICE_PAGES.items():
    pages[filename] = (title, service_body(heading, intro, items), False)

pages["clients.html"] = (
    "Our Clients & Partners | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Portfolio</p><h1>Our Clients &amp; Sectors</h1><p class="lead">We partner with educational institutions, mining operators, utility providers, and commercial enterprises across Zimbabwe.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="service-tile"><h3>Zimbabwe Power</h3><p>Power transmission technicians, electrical engineers, and control-room staff.</p></article>
  <article class="service-tile"><h3>Zimplats Logistics</h3><p>Heavy fleet supervisors, dispatch coordinators, and logistics leads.</p></article>
  <article class="service-tile"><h3>Harare Industrial</h3><p>Plant HR administration, internal audit, and shop-floor manufacturing crews.</p></article>
  <article class="service-tile"><h3>Bulawayo Metals</h3><p>Maintenance technicians, metallurgical specialists, and safety officers.</p></article>
  <article class="service-tile"><h3>Mutare Agro</h3><p>Processing leads, shift supervisors, and payroll administration.</p></article>
  <article class="service-tile"><h3>Gweru Mining</h3><p>Underground supervisors, equipment operators, and site audit functions.</p></article>
</div></section>
""",
    False,
)

pages["locations.html"] = (
    "Our Locations | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Locations</p><h1>Where You Will Find Us</h1><p class="lead">Our consultants operate in key industrial, mining, and commercial centers across Zimbabwe.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="office"><h3>Harare (Head Office)</h3><p>Conrad Forester Investments, Harare Commercial Center.</p><p>Contact: Mavhondo Fanwell Tatenda</p><p>Tel. +263 713 174 032</p></article>
  <article class="office"><h3>Bulawayo</h3><p>Belmont Industrial Area Operations Desk.</p><p>Tel. +263 29 200 0000</p></article>
  <article class="office"><h3>Mutare</h3><p>Eastern Highlands Commercial Suite.</p><p>Tel. +263 20 200 0000</p></article>
  <article class="office"><h3>Gweru</h3><p>Midlands Mining &amp; Industrial Liaison.</p><p>Tel. +263 54 200 0000</p></article>
  <article class="office"><h3>Masvingo</h3><p>Agricultural &amp; Regional Project Desk.</p><p>Tel. +263 39 200 0000</p></article>
  <article class="office"><h3>Johannesburg Liaison</h3><p>Regional SADC Cross-Border Desk.</p><p>Tel. +27 11 000 0000</p></article>
</div></section>
""",
    False,
)

pages["contact.html"] = (
    "Contact Us | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Contact Us</p><h1>Get in Touch</h1><p class="lead">Connect with our consulting team for Internal Audit, Preparation of Final Accounts, Job Appraisals, Training, or Labour Outsourcing in Zimbabwe.</p></div></section>
<section class="section"><div class="wrap split">
  <div>
    <h2>Send a Message</h2>
    <p style="margin-bottom:20px;"><strong>Email:</strong> info@elsewedyconsultancy.com<br><strong>Phone:</strong> +263 713 174 032</p>
    <form class="form" data-demo-form>
      <input name="name" placeholder="Full Name*" required>
      <input name="company" placeholder="Company / Institution*" required>
      <input name="phone" placeholder="Phone Number*" required>
      <input type="email" name="email" placeholder="Email Address*" required>
      <textarea name="message" placeholder="How can we help your organization?*" required></textarea>
      <button class="btn" type="submit">Submit Message</button>
      <p class="notice">Thank you. Your message has been received and a consultant will respond promptly.</p>
    </form>
  </div>
  <div>
    <h2>Office Details</h2>
    <article class="office" style="margin-bottom:16px">
      <strong>Company Registration &amp; Entity</strong>
      <p>Conrad Forester Investments (Reg No: 260/2021)<br>t/a Elsewedy People &amp; Talent</p>
    </article>
    <article class="office" style="margin-bottom:16px">
      <strong>Contact Person</strong>
      <p>Mavhondo Fanwell Tatenda<br>Direct Line: +263 713 174 032<br>Email: info@elsewedyconsultancy.com</p>
    </article>
    <article class="office">
      <strong>Main Operating Locations</strong>
      <p>Harare Commercial Center, Bulawayo Industrial Zone, Mutare &amp; Gweru.</p>
    </article>
  </div>
</div></section>
""",
    False,
)

pages["jobs.html"] = (
    "Vacancies | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Vacancies</p><h1>Open Roles in Zimbabwe</h1><p class="lead">Explore current opportunities across plant management, internal audit, finance, and operations.</p></div></section>
<section class="section"><div class="wrap job-grid">
  <article class="job-card"><span class="tag">Human Resources</span><h3><a href="jobs/plant-hr-bp.html">Plant HR &amp; Operations Lead</a></h3><p>Harare · Full time</p></article>
  <article class="job-card"><span class="tag">Internal Audit</span><h3><a href="jobs/shift-operations-lead.html">Internal Audit &amp; Compliance Officer</a></h3><p>Bulawayo · Full time</p></article>
</div></section>
""",
    False,
)

pages["news.html"] = (
    "News & Insights | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Insights</p><h1>News &amp; Industry Articles</h1><p class="lead">Expert commentary on internal audit, governance, labour law, and workforce training in Zimbabwe.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="news-card"><p class="muted">12 Mar 2026 · Mavhondo Fanwell Tatenda</p><h3><a href="news/skills-for-industry.html">Building Strong Internal Audit &amp; Risk Governance in Schools &amp; Enterprises</a></h3><p>How structured internal controls and governance strengthen financial management and resource allocation.</p></article>
  <article class="news-card"><p class="muted">02 Feb 2026 · Elsewedy Consulting Desk</p><h3><a href="news/workforce-planning.html">Job Appraisals &amp; Labour Compliance under Zimbabwean Regulations</a></h3><p>Designing performance appraisal systems aligned with the Zimbabwean Labour Act.</p></article>
</div></section>
""",
    False,
)

pages["send-cv.html"] = (
    "Send Your CV | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Candidates</p><h1>Submit Your CV</h1><p class="lead">Join our professional talent database for opportunities in Zimbabwe and the SADC region.</p></div></section>
<section class="section"><div class="wrap" style="max-width:640px">
  <form class="form" data-demo-form>
    <input name="name" placeholder="Full Name*" required>
    <input type="email" name="email" placeholder="Email Address*" required>
    <input name="phone" placeholder="Phone Number*" required>
    <select name="interest" required>
      <option value="">Primary Area of Expertise*</option>
      <option>Internal Audit &amp; Financial Control</option>
      <option>Human Resources &amp; Training</option>
      <option>Operations &amp; Manufacturing</option>
      <option>Engineering &amp; Technical</option>
      <option>Supply Chain &amp; Logistics</option>
    </select>
    <input type="file" aria-label="CV file attachment">
    <textarea name="note" placeholder="Brief summary of your career background and career targets"></textarea>
    <button class="btn" type="submit">Submit CV</button>
    <p class="notice">Thank you. Your submission has been received and recorded in our candidate database.</p>
  </form>
</div></section>
""",
    False,
)

pages["search.html"] = (
    "Search Results | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Search</p><h1>Search Results</h1><p class="lead">You searched for: <strong data-query>our services</strong></p></div></section>
<section class="section"><div class="wrap">
  <p>Search across our service solutions, career vacancies, and company insights.</p>
  <p style="margin-top:20px;"><a class="btn" href="jobs.html">View Vacancies</a> <a class="btn btn-ghost" href="hr-consulting.html" style="margin-left:12px;">Explore Audit Services</a></p>
</div></section>
""",
    False,
)

pages["privacy.html"] = (
    "Privacy Policy | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><h1>Privacy Policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>Elsewedy People &amp; Talent (operated by Conrad Forester Investments, Reg No: 260/2021) is committed to protecting the privacy and security of candidate and client information.</p>
  <p>Personal details provided through forms or CV submissions are handled with strict confidentiality in accordance with applicable Zimbabwean data protection laws and statutory regulations.</p>
</div></section>
""",
    False,
)

pages["cookies.html"] = (
    "Cookie Policy | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><h1>Cookie Policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>This website uses essential browser cookies solely to support navigation, site security, and user experience. We do not sell or share personal tracking data with third parties.</p>
</div></section>
""",
    False,
)

pages["jobs/plant-hr-bp.html"] = (
    "Plant HR & Operations Lead | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Human Resources</p><h1>Plant HR &amp; Operations Lead</h1><p>Harare · Full time</p></div></section>
<section class="section"><div class="wrap prose">
  <p>Lead shop-floor employee relations, performance appraisals, manpower planning, and HR compliance for a major manufacturing facility in Harare.</p>
  <h2>Responsibilities</h2>
  <ul class="list-check">
    <li>Oversee manpower allocation, headcount reporting, and job appraisals for plant personnel.</li>
    <li>Manage disciplinary processes in accordance with the Zimbabwean Labour Act [Chapter 28:01].</li>
    <li>Coordinate staff training &amp; development and safety compliance programs.</li>
    <li>Maintain employee attendance records, NSSA files, and statutory filings.</li>
  </ul>
  <h2>Requirements</h2>
  <ul class="list-check">
    <li>Degree in Human Resource Management or related discipline.</li>
    <li>Minimum 4 years HR leadership experience in manufacturing or industrial sectors.</li>
    <li>In-depth knowledge of Zimbabwean Labour Law and statutory requirements.</li>
  </ul>
  <p style="margin-top:24px"><a class="btn" href="../send-cv.html">Apply with Your CV</a></p>
</div></section>
""",
    True,
)

pages["jobs/shift-operations-lead.html"] = (
    "Internal Audit & Compliance Officer | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Internal Audit</p><h1>Internal Audit &amp; Compliance Officer</h1><p>Bulawayo · Full time</p></div></section>
<section class="section"><div class="wrap prose">
  <p>Conduct objective internal audit evaluations, review internal controls, verify preparation of final accounts, and ensure regulatory compliance for institutional and commercial clients in Bulawayo.</p>
  <h2>Responsibilities</h2>
  <ul class="list-check">
    <li>Execute internal financial audits, operational reviews, and compliance testing.</li>
    <li>Evaluate internal control environments and provide risk management recommendations.</li>
    <li>Assist in reviewing and preparing final accounts for corporate clients and educational institutions.</li>
    <li>Draft concise audit reports and present findings to executive leadership and boards.</li>
  </ul>
  <h2>Requirements</h2>
  <ul class="list-check">
    <li>Degree in Accounting, Finance, or Auditing (CIA, ACCA, or CIS qualification preferred).</li>
    <li>3+ years in internal or external auditing within Zimbabwe.</li>
    <li>Strong analytical skills and familiarity with IAS/IFRS accounting standards.</li>
  </ul>
  <p style="margin-top:24px"><a class="btn" href="../send-cv.html">Apply with Your CV</a></p>
</div></section>
""",
    True,
)

pages["news/skills-for-industry.html"] = (
    "Internal Audit & Governance | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="muted">12 Mar 2026 · Mavhondo Fanwell Tatenda</p><h1>Building Strong Internal Audit &amp; Risk Governance in Schools &amp; Enterprises</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>Robust operational and financial performance relies on solid internal audit functions and clear governance frameworks. When schools and commercial organizations implement objective internal audit mechanisms, resource management improves and risk is mitigated proactively.</p>
  <p>At Conrad Forester Investments t/a Elsewedy People &amp; Talent, we help institutions strengthen governance structures, ensure statutory compliance, and streamline internal control systems for sustainable growth across Zimbabwe.</p>
  <p style="margin-top:24px"><a href="../news.html">← Back to News &amp; Insights</a></p>
</div></section>
""",
    True,
)

pages["news/workforce-planning.html"] = (
    "Job Appraisals & Labour Compliance | Elsewedy Zimbabwe",
    """
<section class="page-hero"><div class="wrap"><p class="muted">02 Feb 2026 · Elsewedy Consulting Desk</p><h1>Job Appraisals &amp; Labour Compliance under Zimbabwean Regulations</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>Effective workforce management requires systematic job appraisals aligned with clear operational objectives and the Zimbabwean Labour Act [Chapter 28:01]. Modern industrial and corporate environments benefit when employee evaluations are transparent and tied to continuous training and development.</p>
  <p>Our consulting desk supports organizations in establishing structured job appraisal frameworks and compliant labour outsourcing models across Harare, Bulawayo, and regional centers.</p>
  <p style="margin-top:24px"><a href="../news.html">← Back to News &amp; Insights</a></p>
</div></section>
""",
    True,
)

for path, (title, body, nested) in pages.items():
    page(path, title, body, nested)

print(f"Successfully generated {len(pages)} pages.")
