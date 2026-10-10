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
<body>
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
          <a href="{r}hr-consulting.html">HR Consulting</a>
          <a href="{r}salary-surveys.html">Salary &amp; Benefits Surveys</a>
        </div>
      </li>
      <li>
        <a href="{r}outsourcing.html">HR Services <i class="caret"></i></a>
        <div class="submenu">
          <a href="{r}outsourcing.html">Outsourcing</a>
          <a href="{r}payroll.html">Payroll Outsourcing</a>
          <a href="{r}employer-of-record.html">Employer of Record</a>
          <a href="{r}labour-law.html">Egypt Labour Law Consulting</a>
          <a href="{r}government-affairs.html">Governmental Affairs Solutions</a>
          <a href="{r}talent-management.html">Talent Management</a>
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
      <h4>Elsewedy People</h4>
      <p>Original human-capital pages for industrial, energy, and corporate teams across Egypt and the region. Layout inspired by typical HR-agency sites; all wording and marks here are new.</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="{r}executive-search.html">Executive Search</a></li>
        <li><a href="{r}outsourcing.html">Workforce Outsourcing</a></li>
        <li><a href="{r}payroll.html">Payroll</a></li>
        <li><a href="{r}hr-consulting.html">HR Consulting</a></li>
      </ul>
    </div>
    <div>
      <h4>For candidates</h4>
      <ul>
        <li><a href="{r}jobs.html">Open vacancies</a></li>
        <li><a href="{r}send-cv.html">Send your CV</a></li>
        <li><a href="{r}candidate-profiles.html">Talent community</a></li>
        <li><a href="{r}news.html">News</a></li>
      </ul>
    </div>
    <div>
      <h4>Offices</h4>
      <ul>
        <li>New Cairo</li>
        <li>10th of Ramadan</li>
        <li>6th of October</li>
        <li><a href="{r}contact.html">Contact the desk</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>© <span data-year></span> Elsewedy People. Demo site with original copy.</span>
    <span>
      <a href="{r}privacy.html">Privacy Policy</a>
      ·
      <a href="{r}cookies.html">Cookie Policy</a>
      ·
      <a href="{r}contact.html">Contact</a>
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
    "People & Talent | Elsewedy People",
    """
<section class="hero">
  <div class="wrap hero-inner">
    <p class="eyebrow">Industrial talent partner in Egypt</p>
    <h1>Build crews,<br>leadership,<br>and HR operations.</h1>
    <a class="btn" href="outsourcing.html">Workforce outsourcing</a>
  </div>
</section>
<section class="section">
  <div class="wrap center">
    <p class="muted">Operators we staff and support</p>
    <div class="clients">
      <div class="client-mark">NILE GRID</div>
      <div class="client-mark">DELTA PORTS</div>
      <div class="client-mark">QATTARA STEEL</div>
      <div class="client-mark">RED SEA LOGISTICS</div>
      <div class="client-mark">CAIRO UTILITIES</div>
      <div class="client-mark">SINAI CEMENT</div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div>
      <p class="kicker">How we hire</p>
      <h2>Structured hiring for plants, projects, and corporate offices.</h2>
      <p class="lead">Elsewedy People runs search, outsourcing, and HR operations for manufacturers, contractors, and energy businesses. We keep hiring conversations equally clear with hiring managers and candidates.</p>
      <div class="cards-2">
        <article class="card">
          <h3>Leadership search</h3>
          <p>Plant directors, finance controllers, and technical heads mapped against a live talent bench.</p>
          <a href="executive-search.html">Learn more</a>
        </article>
        <article class="card">
          <h3>Crew staffing</h3>
          <p>Blue-collar and technician pipelines for factories, sites, and warehouses across Egypt.</p>
          <a href="global-staffing.html">Learn more</a>
        </article>
      </div>
    </div>
    <div class="photo" style="background-image:linear-gradient(rgba(0,0,0,.15),rgba(0,0,0,.15)), url('assets/img/hero.svg')">
      <span class="badge-circle"></span>
    </div>
  </div>
</section>
<section class="section panel">
  <div class="wrap stats">
    <div>
      <p class="kicker" style="color:#f3b2a8">Scale</p>
      <div class="stat-num">2,400+</div>
      <p>People on outsourced assignments this year</p>
    </div>
    <div class="pillars">
      <div class="pillar">
        <div class="icon-box">01</div>
        <div>
          <strong>HR operations</strong>
          <div class="muted">Contracts, social insurance, and plant-level employee care.</div>
        </div>
        <a href="hr-consulting.html">Our HR solutions</a>
      </div>
      <div class="pillar">
        <div class="icon-box">02</div>
        <div>
          <strong>Talent files</strong>
          <div class="muted">Assessed supervisors and specialists ready for shortlists.</div>
        </div>
        <a href="candidate-profiles.html">Candidate profiles</a>
      </div>
      <div class="pillar">
        <div class="icon-box">03</div>
        <div>
          <strong>Open roles</strong>
          <div class="muted">Live vacancies for operators, engineers, and office teams.</div>
        </div>
        <a href="jobs.html">Our vacancies</a>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="jobs-head">
      <div>
        <p class="kicker">Careers</p>
        <h2>What role are you targeting?</h2>
        <p class="muted">Upload a CV and we will match you to current and upcoming briefs.</p>
      </div>
      <a class="btn" href="send-cv.html">Upload your CV</a>
    </div>
    <div class="job-grid">
      <article class="job-card">
        <span class="tag">Human Resources</span>
        <h3><a href="jobs/plant-hr-bp.html">Plant HR Business Partner</a></h3>
        <p>Own employee relations, headcount, and shop-floor HR for a cable and metals campus in 10th of Ramadan.</p>
        <a href="jobs/plant-hr-bp.html">Read more</a>
      </article>
      <article class="job-card">
        <span class="tag">Operations</span>
        <h3><a href="jobs/shift-operations-lead.html">Shift Operations Lead — Distribution</a></h3>
        <p>Run night and weekend shifts for a high-volume warehouse serving industrial customers in Greater Cairo.</p>
        <a href="jobs/shift-operations-lead.html">Read more</a>
      </article>
    </div>
  </div>
</section>
<section class="section" style="background:var(--paper)">
  <div class="wrap split">
    <div>
      <p class="kicker">Clients</p>
      <h2>A people desk for industrial groups.</h2>
      <p>We handle confidential searches, volume hiring, and day-to-day HR administration so plant leaders can stay on output, safety, and delivery.</p>
      <a class="btn" href="contact.html">Talk to the desk</a>
    </div>
    <form class="form card" data-demo-form>
      <h3>Request a briefing</h3>
      <input name="name" placeholder="Name*" required>
      <input name="company" placeholder="Company*" required>
      <input name="phone" placeholder="Phone*" required>
      <input type="email" name="email" placeholder="Email*" required>
      <textarea name="message" placeholder="Message*" required></textarea>
      <button class="btn" type="submit">Submit</button>
      <p class="notice">Thanks. This demo form stays on your machine and is not sent to a server.</p>
    </form>
  </div>
</section>
""",
    False,
)

SERVICE_PAGES = {
    "executive-search.html": (
        "Executive Search | Elsewedy People",
        "Executive search",
        "We map leadership benches for factories, project companies, and group functions. Searches stay confidential, criteria are written with the hiring panel, and shortlists include work evidence rather than recycled CVs.",
        [
            "Plant, operations, and technical directors",
            "Finance, HR, and commercial controllers",
            "Confidential replacements and first-time country roles",
            "90-day onboarding notes for the successful hire",
        ],
    ),
    "candidate-profiles.html": (
        "Candidate Profiles | Elsewedy People",
        "Candidate profiles",
        "Assessed talent files for supervisors, engineers, and specialists who already know industrial environments. Profiles include availability, compensation bands, and language mix.",
        [
            "Pre-screened technical and plant talent",
            "Competency notes from structured interviews",
            "Consent-based sharing with named clients only",
            "Refresh cycle every 90 days",
        ],
    ),
    "psychometric.html": (
        "Psychometric Testing | Elsewedy People",
        "Psychometric testing",
        "Ability and work-style assessments used as one input beside interviews and technical trials. We brief hiring managers on what a score can and cannot tell them.",
        [
            "Reasoning and numerical screens for professional roles",
            "Supervisor judgement and safety-behaviour tools",
            "Arabic and English administration",
            "Feedback sessions for finalists on request",
        ],
    ),
    "placement.html": (
        "Placement Services | Elsewedy People",
        "Placement services",
        "End-to-end placement for mid-level professional and technician roles: briefing, sourcing, interviews, offers, and joining checks.",
        [
            "Role scorecards written with the line manager",
            "Market mapping across Cairo, Alexandria, and industrial cities",
            "Offer calibration against current pay data",
            "30-day joining follow-up",
        ],
    ),
    "hr-systems.html": (
        "HR Systems | Elsewedy People",
        "HR systems",
        "Practical help selecting, configuring, and cleaning HRIS data so headcount, leave, and payroll files match the shop floor.",
        [
            "Process design before software choice",
            "Data clean-up and organisational trees",
            "Manager self-service rollouts",
            "Reporting packs for plant and group HR",
        ],
    ),
    "hr-consulting.html": (
        "HR Consulting | Elsewedy People",
        "HR consulting",
        "Project work for companies that need policies, structures, or performance routines that actually run in factories and project sites, not only head office.",
        [
            "Job architecture and descriptions",
            "HR policy and employee handbook updates",
            "Performance and KPI calendars",
            "Restructuring and rightsizing support",
        ],
    ),
    "salary-surveys.html": (
        "Salary & Benefits Surveys | Elsewedy People",
        "Salary and benefits surveys",
        "Confidential pay snapshots for industrial and corporate families in Egypt, used to set ranges before offers go out.",
        [
            "Role matching to a common catalogue",
            "Base, allowances, and variable pay",
            "Shift and hardship premiums",
            "Board-ready summary charts",
        ],
    ),
    "outsourcing.html": (
        "Workforce Outsourcing | Elsewedy People",
        "Workforce outsourcing",
        "We employ assigned staff, run personnel files, and coordinate attendance with your supervisors. You keep day-to-day direction of the work.",
        [
            "Employment contracts and onboarding",
            "Social insurance and medical coordination",
            "Site HR presence where volumes justify it",
            "Exit files and knowledge handback",
        ],
    ),
    "payroll.html": (
        "Payroll Outsourcing | Elsewedy People",
        "Payroll outsourcing",
        "Monthly payroll calculation, statutory deductions, and payslip delivery for outsourced and client-employed populations.",
        [
            "Attendance to net-pay controls",
            "Tax and social insurance filings support",
            "Bank file generation",
            "Audit trails for internal and external reviews",
        ],
    ),
    "employer-of-record.html": (
        "Employer of Record | Elsewedy People",
        "Employer of record",
        "A compliant Egyptian employer of record for specialists you need on the ground quickly, without standing up a full local entity first.",
        [
            "Local employment contracts",
            "Payroll, leave, and benefits administration",
            "Workplace policy coverage",
            "Clear conversion path if you later hire directly",
        ],
    ),
    "labour-law.html": (
        "Egypt Labour Law Consulting | Elsewedy People",
        "Egypt labour law consulting",
        "Briefings and case support on contracts, working time, discipline, and termination so managers do not improvise on the floor.",
        [
            "Contract templates by worker category",
            "Disciplinary process coaching",
            "Collective issue triage",
            "Updates when regulations change",
        ],
    ),
    "government-affairs.html": (
        "Governmental Affairs | Elsewedy People",
        "Governmental affairs",
        "Coordination of labour-office, insurance, and workforce filings that industrial employers cannot stall without stopping production.",
        [
            "Workforce authorization files",
            "Inspection preparation",
            "Insurance account follow-up",
            "Document tracking with named owners",
        ],
    ),
    "talent-management.html": (
        "Talent Management | Elsewedy People",
        "Talent management",
        "Succession, technician academies, and supervisor pipelines so plants are not one resignation away from a stoppage.",
        [
            "Critical-role maps",
            "Internal shortlists and stretch assignments",
            "Supervisor skill sprints",
            "Graduate and technician intake programmes",
        ],
    ),
    "employer-branding.html": (
        "Employment Branding | Elsewedy People",
        "Employment branding",
        "Clear employer stories for industrial sites that struggle to attract technicians and first-line leaders.",
        [
            "Site walk-through narratives",
            "Hiring-manager interview toolkits",
            "Campus and trade-school presence",
            "Offer-process redesign",
        ],
    ),
    "employment-outsourcing.html": (
        "Global Employment Outsourcing | Elsewedy People",
        "Global employment outsourcing",
        "Cross-border employment support when a regional project needs people in Egypt and a second country under one programme manager.",
        [
            "Multi-country onboarding checklists",
            "Pay and benefit alignment notes",
            "Local partner coordination",
            "Single client reporting pack",
        ],
    ),
    "global-staffing.html": (
        "Global Staffing | Elsewedy People",
        "Global staffing",
        "Project and rotational staffing for energy, construction, and manufacturing programmes that move people between Egypt and neighbouring markets.",
        [
            "Technician and engineer rosters",
            "Mobilisation calendars",
            "Client site rules briefed before travel",
            "Demobilisation and knowledge capture",
        ],
    ),
    "work-permits.html": (
        "Work Permits & Visas | Elsewedy People",
        "Work permits and visas",
        "File preparation and tracking for expatriate specialists who need lawful work status in Egypt.",
        [
            "Document checklists by nationality",
            "Ministry file tracking",
            "Family accompaniment notes",
            "Renewal calendars",
        ],
    ),
    "attestation.html": (
        "Attestation Services | Elsewedy People",
        "Attestation services",
        "Education, police, and corporate document attestation support used in hiring and mobility files.",
        [
            "Degree and certificate chains",
            "Commercial document packs",
            "Translation coordination",
            "Status updates until pickup",
        ],
    ),
}


def service_body(heading: str, intro: str, items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Service</p>
    <h1>{heading}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div>
      <h2>What you get</h2>
      <ul class="list-check">{lis}</ul>
      <p style="margin-top:24px"><a class="btn" href="contact.html">Request a briefing</a></p>
    </div>
    <aside class="card">
      <h3>Typical clients</h3>
      <p>Plant HR, shared-services leads, and project directors who need a named consultant rather than a generic mailbox.</p>
      <p class="muted">All pages on this demo use original wording written for the Elsewedy People project.</p>
    </aside>
  </div>
</section>
"""


for filename, (title, heading, intro, items) in SERVICE_PAGES.items():
    pages[filename] = (title, service_body(heading, intro, items), False)

pages["clients.html"] = (
    "Our Clients | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Portfolio</p><h1>Our clients</h1><p class="lead">We staff and support industrial operators, utilities, and project companies. Names below are illustrative marks for this demo.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="service-tile"><h3>Nile Grid</h3><p>Transmission and substation crews plus control-room specialists.</p></article>
  <article class="service-tile"><h3>Delta Ports</h3><p>Shift supervisors and equipment operators for bulk terminals.</p></article>
  <article class="service-tile"><h3>Qattara Steel</h3><p>Maintenance technicians and plant HR support.</p></article>
  <article class="service-tile"><h3>Red Sea Logistics</h3><p>Warehouse leads and transport coordinators.</p></article>
  <article class="service-tile"><h3>Cairo Utilities</h3><p>Field engineers and customer operations roles.</p></article>
  <article class="service-tile"><h3>Sinai Cement</h3><p>Production supervisors and safety officers.</p></article>
</div></section>
""",
    False,
)

pages["locations.html"] = (
    "Our Locations | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Offices</p><h1>Where you will find us</h1><p class="lead">Desks sit next to the industrial corridors we hire for. Phone numbers below are placeholders for this static demo.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="office"><h3>New Cairo</h3><p>Cairo Festival City district, 5th Settlement.</p><p>Tel. +20 2 0000 0000</p></article>
  <article class="office"><h3>10th of Ramadan</h3><p>Plant-side desk for cables, metals, and factories.</p><p>Tel. +20 15 0000 0000</p></article>
  <article class="office"><h3>6th of October</h3><p>Industrial Zone coordination for meters and assembly.</p><p>Tel. +20 11 0000 0000</p></article>
  <article class="office"><h3>Alexandria</h3><p>Coastal projects and port-linked hiring.</p><p>Tel. +20 3 0000 0000</p></article>
  <article class="office"><h3>Dubai desk</h3><p>Regional mobility and Gulf project staffing.</p><p>Tel. +971 0 000 0000</p></article>
  <article class="office"><h3>Birmingham liaison</h3><p>Supplier and specialist search support.</p><p>Tel. +44 121 000 0000</p></article>
</div></section>
""",
    False,
)

pages["contact.html"] = (
    "Contact | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Contact</p><h1>Contact us</h1><p class="lead">Reach the people desk any working day. Forms on this demo stay in the browser.</p></div></section>
<section class="section"><div class="wrap split">
  <div>
    <h2>Send a message</h2>
    <p>people@elsewedy.example</p>
    <form class="form" data-demo-form>
      <input name="name" placeholder="Name*" required>
      <input name="company" placeholder="Company*" required>
      <input name="phone" placeholder="Phone*" required>
      <input type="email" name="email" placeholder="Email*" required>
      <textarea name="message" placeholder="Message*" required></textarea>
      <button class="btn" type="submit">Submit</button>
      <p class="notice">Message captured locally only. Connect a backend when you are ready to go live.</p>
    </form>
  </div>
  <div>
    <h2>Where you will find us</h2>
    <article class="office"><strong>Egypt — Cairo</strong><p>Cairo Festival City, 5th Settlement, New Cairo.</p></article>
    <article class="office"><strong>10th of Ramadan</strong><p>Plant HR coordination desk.</p></article>
    <article class="office"><strong>6th of October</strong><p>Industrial Zone 2 liaison.</p></article>
  </div>
</div></section>
""",
    False,
)

pages["jobs.html"] = (
    "Vacancies | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Vacancies</p><h1>Open roles</h1><p class="lead">Sample vacancies written for this project. Apply by sending a CV through the form on each role.</p></div></section>
<section class="section"><div class="wrap job-grid">
  <article class="job-card"><span class="tag">Human Resources</span><h3><a href="jobs/plant-hr-bp.html">Plant HR Business Partner</a></h3><p>10th of Ramadan · Full time</p></article>
  <article class="job-card"><span class="tag">Operations</span><h3><a href="jobs/shift-operations-lead.html">Shift Operations Lead — Distribution</a></h3><p>Greater Cairo · Full time</p></article>
</div></section>
""",
    False,
)

pages["news.html"] = (
    "News | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Insights</p><h1>News</h1><p class="lead">Original notes on industrial workforce topics. Not syndicated from other agencies.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="news-card"><p class="muted">12 Mar 2026 · Lina Farouk</p><h3><a href="news/skills-for-industry.html">Technician pipelines for expanding plants</a></h3><p>Why three-year craft academies beat last-minute overtime when a new line starts.</p></article>
  <article class="news-card"><p class="muted">02 Feb 2026 · Karim Nassar</p><h3><a href="news/workforce-planning.html">Headcount plans that survive a shutdown week</a></h3><p>A simple rolling view of absences, contractors, and critical tickets.</p></article>
</div></section>
""",
    False,
)

pages["send-cv.html"] = (
    "Send your CV | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Candidates</p><h1>Send your CV</h1><p class="lead">Join the talent community. Files are not uploaded in this static demo.</p></div></section>
<section class="section"><div class="wrap" style="max-width:640px">
  <form class="form" data-demo-form>
    <input name="name" placeholder="Full name*" required>
    <input type="email" name="email" placeholder="Email*" required>
    <input name="phone" placeholder="Phone*" required>
    <select name="interest" required>
      <option value="">Function of interest*</option>
      <option>Operations &amp; manufacturing</option>
      <option>Engineering</option>
      <option>Human resources</option>
      <option>Finance</option>
      <option>Supply chain</option>
    </select>
    <input type="file" aria-label="CV file">
    <textarea name="note" placeholder="A short note on the roles you want"></textarea>
    <button class="btn" type="submit">Submit CV</button>
    <p class="notice">Thanks. Wire this form to your ATS before launch.</p>
  </form>
</div></section>
""",
    False,
)

pages["search.html"] = (
    "Search | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Search</p><h1>Results</h1><p class="lead">You searched for: <strong data-query>all pages</strong></p></div></section>
<section class="section"><div class="wrap">
  <p>This static demo does not run a search index. Browse services, jobs, and news from the header.</p>
  <p><a class="btn" href="jobs.html">View vacancies</a></p>
</div></section>
""",
    False,
)

pages["privacy.html"] = (
    "Privacy Policy | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><h1>Privacy policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>This demonstration website does not collect personal data on a server. Forms show an on-page confirmation only.</p>
  <p>If you later connect hosting, analytics, or an ATS, publish a full notice covering the controller, purposes, retention, and candidate rights under applicable Egyptian law.</p>
</div></section>
""",
    False,
)

pages["cookies.html"] = (
    "Cookie Policy | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><h1>Cookie policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>This static demo does not set tracking cookies. A future production host may use essential cookies for session security.</p>
</div></section>
""",
    False,
)

pages["jobs/plant-hr-bp.html"] = (
    "Plant HR Business Partner | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Human Resources</p><h1>Plant HR Business Partner</h1><p>10th of Ramadan · Full time</p></div></section>
<section class="section"><div class="wrap prose">
  <p>You will sit with production and maintenance leaders, keep headcount true, and run employee relations that shop-floor teams actually trust.</p>
  <h2>You will</h2>
  <ul class="list-check">
    <li>Own manpower reports and vacancy tracking for the campus.</li>
    <li>Coordinate onboarding, attendance exceptions, and disciplinary files.</li>
    <li>Partner with L&amp;D on technician and supervisor programmes.</li>
    <li>Maintain HRIS records and monthly analytics.</li>
  </ul>
  <h2>You bring</h2>
  <ul class="list-check">
    <li>Three or more years as an HR generalist in manufacturing.</li>
    <li>Comfort with Egyptian labour-law basics and insurance files.</li>
    <li>Excel or Power BI reporting you can defend in a plant meeting.</li>
  </ul>
  <p><a class="btn" href="../send-cv.html">Apply with your CV</a></p>
</div></section>
""",
    True,
)

pages["jobs/shift-operations-lead.html"] = (
    "Shift Operations Lead | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="kicker">Operations</p><h1>Shift Operations Lead — Distribution</h1><p>Greater Cairo · Full time</p></div></section>
<section class="section"><div class="wrap prose">
  <p>Lead a warehouse shift serving industrial customers: throughput, safety talks, and a calm radio when the dock gets noisy.</p>
  <h2>You will</h2>
  <ul class="list-check">
    <li>Plan labour for inbound, put-away, and dispatch.</li>
    <li>Run start-of-shift briefings and incident notes.</li>
    <li>Escalate equipment and system issues before they stop the line.</li>
  </ul>
  <h2>You bring</h2>
  <ul class="list-check">
    <li>Prior shift leadership in warehousing, FMCG, or manufacturing.</li>
    <li>Arabic and working English.</li>
    <li>Willingness for rotating nights and weekends.</li>
  </ul>
  <p><a class="btn" href="../send-cv.html">Apply with your CV</a></p>
</div></section>
""",
    True,
)

pages["news/skills-for-industry.html"] = (
    "Technician pipelines | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="muted">12 Mar 2026 · Lina Farouk</p><h1>Technician pipelines for expanding plants</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>When a new line is announced, overtime hides the real gap for about six weeks. After that, quality and safety start to show the missing craft skills.</p>
  <p>A workable pipeline names the three craft families the plant cannot borrow from contractors, funds a shared workshop with a technical school, and puts a supervisor in the room every Friday. Elsewedy People uses that pattern on industrial campuses so hiring is not a last-week scramble.</p>
  <p><a href="../news.html">Back to news</a></p>
</div></section>
""",
    True,
)

pages["news/workforce-planning.html"] = (
    "Workforce planning | Elsewedy People",
    """
<section class="page-hero"><div class="wrap"><p class="muted">02 Feb 2026 · Karim Nassar</p><h1>Headcount plans that survive a shutdown week</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>Annual headcount files go stale the first time a furnace trips. A living plan tracks three numbers weekly: people at work, people absent, and tickets that only a named craft can close.</p>
  <p>We keep that view with plant HR so outsourcing top-ups are a decision, not a surprise invoice.</p>
  <p><a href="../news.html">Back to news</a></p>
</div></section>
""",
    True,
)

for path, (title, body, nested) in pages.items():
    page(path, title, body, nested)

print(f"Wrote {len(pages)} pages")
