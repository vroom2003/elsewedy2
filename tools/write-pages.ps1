$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

function Get-Doc($Title, $RootPrefix, $Body) {
  @"
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$Title</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="${RootPrefix}assets/css/main.css">
  <link rel="icon" href="${RootPrefix}assets/img/logo.svg">
</head>
<body data-root="$RootPrefix">
<a class="skip" href="#main">Skip to content</a>
<div data-include="header"></div>
<main id="main">
$Body
</main>
<div data-include="footer"></div>
<script src="${RootPrefix}assets/js/chrome.js"></script>
<script src="${RootPrefix}assets/js/site.js"></script>
</body>
</html>
"@
}

function Write-Page($RelPath, $Title, $Body, $Nested = $false) {
  $prefix = if ($Nested) { "../" } else { "" }
  $path = Join-Path $root $RelPath
  $dir = Split-Path -Parent $path
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
  $html = Get-Doc $Title $prefix $Body
  Set-Content -Path $path -Value $html -Encoding UTF8
  Write-Output $RelPath
}

function Service-Body($Heading, $Intro, $Items) {
  $lis = ($Items | ForEach-Object { "<li>$_</li>" }) -join ""
  @"
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Service</p>
    <h1>$Heading</h1>
    <p class="lead">$Intro</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div>
      <h2>What you get</h2>
      <ul class="list-check">$lis</ul>
      <p style="margin-top:24px"><a class="btn" href="contact.html">Request a briefing</a></p>
    </div>
    <aside class="card">
      <h3>Typical clients</h3>
      <p>Plant HR, shared-services leads, and project directors who need a named consultant rather than a generic mailbox.</p>
      <p class="muted">All pages on this demo use original wording written for the Elsewedy People project.</p>
    </aside>
  </div>
</section>
"@
}

$services = @(
  @{ f="executive-search.html"; t="Executive Search | Elsewedy People"; h="Executive search"; i="We map leadership benches for factories, project companies, and group functions. Searches stay confidential, criteria are written with the hiring panel, and shortlists include work evidence rather than recycled CVs."; items=@("Plant, operations, and technical directors","Finance, HR, and commercial controllers","Confidential replacements and first-time country roles","90-day onboarding notes for the successful hire") }
  @{ f="candidate-profiles.html"; t="Candidate Profiles | Elsewedy People"; h="Candidate profiles"; i="Assessed talent files for supervisors, engineers, and specialists who already know industrial environments. Profiles include availability, compensation bands, and language mix."; items=@("Pre-screened technical and plant talent","Competency notes from structured interviews","Consent-based sharing with named clients only","Refresh cycle every 90 days") }
  @{ f="psychometric.html"; t="Psychometric Testing | Elsewedy People"; h="Psychometric testing"; i="Ability and work-style assessments used as one input beside interviews and technical trials. We brief hiring managers on what a score can and cannot tell them."; items=@("Reasoning and numerical screens for professional roles","Supervisor judgement and safety-behaviour tools","Arabic and English administration","Feedback sessions for finalists on request") }
  @{ f="placement.html"; t="Placement Services | Elsewedy People"; h="Placement services"; i="End-to-end placement for mid-level professional and technician roles: briefing, sourcing, interviews, offers, and joining checks."; items=@("Role scorecards written with the line manager","Market mapping across Cairo, Alexandria, and industrial cities","Offer calibration against current pay data","30-day joining follow-up") }
  @{ f="hr-systems.html"; t="HR Systems | Elsewedy People"; h="HR systems"; i="Practical help selecting, configuring, and cleaning HRIS data so headcount, leave, and payroll files match the shop floor."; items=@("Process design before software choice","Data clean-up and organisational trees","Manager self-service rollouts","Reporting packs for plant and group HR") }
  @{ f="hr-consulting.html"; t="HR Consulting | Elsewedy People"; h="HR consulting"; i="Project work for companies that need policies, structures, or performance routines that actually run in factories and project sites, not only head office."; items=@("Job architecture and descriptions","HR policy and employee handbook updates","Performance and KPI calendars","Restructuring and rightsizing support") }
  @{ f="salary-surveys.html"; t="Salary &amp; Benefits Surveys | Elsewedy People"; h="Salary and benefits surveys"; i="Confidential pay snapshots for industrial and corporate families in Egypt, used to set ranges before offers go out."; items=@("Role matching to a common catalogue","Base, allowances, and variable pay","Shift and hardship premiums","Board-ready summary charts") }
  @{ f="outsourcing.html"; t="Workforce Outsourcing | Elsewedy People"; h="Workforce outsourcing"; i="We employ assigned staff, run personnel files, and coordinate attendance with your supervisors. You keep day-to-day direction of the work."; items=@("Employment contracts and onboarding","Social insurance and medical coordination","Site HR presence where volumes justify it","Exit files and knowledge handback") }
  @{ f="payroll.html"; t="Payroll Outsourcing | Elsewedy People"; h="Payroll outsourcing"; i="Monthly payroll calculation, statutory deductions, and payslip delivery for outsourced and client-employed populations."; items=@("Attendance to net-pay controls","Tax and social insurance filings support","Bank file generation","Audit trails for internal and external reviews") }
  @{ f="employer-of-record.html"; t="Employer of Record | Elsewedy People"; h="Employer of record"; i="A compliant Egyptian employer of record for specialists you need on the ground quickly, without standing up a full local entity first."; items=@("Local employment contracts","Payroll, leave, and benefits administration","Workplace policy coverage","Clear conversion path if you later hire directly") }
  @{ f="labour-law.html"; t="Egypt Labour Law Consulting | Elsewedy People"; h="Egypt labour law consulting"; i="Briefings and case support on contracts, working time, discipline, and termination so managers do not improvise on the floor."; items=@("Contract templates by worker category","Disciplinary process coaching","Collective issue triage","Updates when regulations change") }
  @{ f="government-affairs.html"; t="Governmental Affairs | Elsewedy People"; h="Governmental affairs"; i="Coordination of labour-office, insurance, and workforce filings that industrial employers cannot stall without stopping production."; items=@("Workforce authorization files","Inspection preparation","Insurance account follow-up","Document tracking with named owners") }
  @{ f="talent-management.html"; t="Talent Management | Elsewedy People"; h="Talent management"; i="Succession, technician academies, and supervisor pipelines so plants are not one resignation away from a stoppage."; items=@("Critical-role maps","Internal shortlists and stretch assignments","Supervisor skill sprints","Graduate and technician intake programmes") }
  @{ f="employer-branding.html"; t="Employment Branding | Elsewedy People"; h="Employment branding"; i="Clear employer stories for industrial sites that struggle to attract technicians and first-line leaders."; items=@("Site walk-through narratives","Hiring-manager interview toolkits","Campus and trade-school presence","Offer-process redesign") }
  @{ f="employment-outsourcing.html"; t="Global Employment Outsourcing | Elsewedy People"; h="Global employment outsourcing"; i="Cross-border employment support when a regional project needs people in Egypt and a second country under one programme manager."; items=@("Multi-country onboarding checklists","Pay and benefit alignment notes","Local partner coordination","Single client reporting pack") }
  @{ f="global-staffing.html"; t="Global Staffing | Elsewedy People"; h="Global staffing"; i="Project and rotational staffing for energy, construction, and manufacturing programmes that move people between Egypt and neighbouring markets."; items=@("Technician and engineer rosters","Mobilisation calendars","Client site rules briefed before travel","Demobilisation and knowledge capture") }
  @{ f="work-permits.html"; t="Work Permits &amp; Visas | Elsewedy People"; h="Work permits and visas"; i="File preparation and tracking for expatriate specialists who need lawful work status in Egypt."; items=@("Document checklists by nationality","Ministry file tracking","Family accompaniment notes","Renewal calendars") }
  @{ f="attestation.html"; t="Attestation Services | Elsewedy People"; h="Attestation services"; i="Education, police, and corporate document attestation support used in hiring and mobility files."; items=@("Degree and certificate chains","Commercial document packs","Translation coordination","Status updates until pickup") }
)

foreach ($s in $services) {
  Write-Page $s.f $s.t (Service-Body $s.h $s.i $s.items)
}

Write-Page "clients.html" "Our Clients | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="kicker">Portfolio</p><h1>Our clients</h1><p class="lead">We staff and support industrial operators, utilities, and project companies. Names below are illustrative marks for this demo.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="service-tile"><h3>Nile Grid</h3><p>Transmission and substation crews plus control-room specialists.</p></article>
  <article class="service-tile"><h3>Delta Ports</h3><p>Shift supervisors and equipment operators for bulk terminals.</p></article>
  <article class="service-tile"><h3>Qattara Steel</h3><p>Maintenance technicians and plant HR support.</p></article>
  <article class="service-tile"><h3>Red Sea Logistics</h3><p>Warehouse leads and transport coordinators.</p></article>
  <article class="service-tile"><h3>Cairo Utilities</h3><p>Field engineers and customer operations roles.</p></article>
  <article class="service-tile"><h3>Sinai Cement</h3><p>Production supervisors and safety officers.</p></article>
</div></section>
"@

Write-Page "locations.html" "Our Locations | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="kicker">Offices</p><h1>Where you will find us</h1><p class="lead">Desks sit next to the industrial corridors we hire for. Phone numbers below are placeholders for this static demo.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="office"><h3>New Cairo</h3><p>Cairo Festival City district, 5th Settlement.</p><p>Tel. +20 2 0000 0000</p></article>
  <article class="office"><h3>10th of Ramadan</h3><p>Plant-side desk for cables, metals, and factories.</p><p>Tel. +20 15 0000 0000</p></article>
  <article class="office"><h3>6th of October</h3><p>Industrial Zone coordination for meters and assembly.</p><p>Tel. +20 11 0000 0000</p></article>
  <article class="office"><h3>Alexandria</h3><p>Coastal projects and port-linked hiring.</p><p>Tel. +20 3 0000 0000</p></article>
  <article class="office"><h3>Dubai desk</h3><p>Regional mobility and Gulf project staffing.</p><p>Tel. +971 0 000 0000</p></article>
  <article class="office"><h3>Birmingham liaison</h3><p>Supplier and specialist search support.</p><p>Tel. +44 121 000 0000</p></article>
</div></section>
"@

Write-Page "jobs.html" "Vacancies | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="kicker">Vacancies</p><h1>Open roles</h1><p class="lead">Sample vacancies written for this project. Apply by sending a CV through the form on each role.</p></div></section>
<section class="section"><div class="wrap job-grid">
  <article class="job-card"><span class="tag">Human Resources</span><h3><a href="jobs/plant-hr-bp.html">Plant HR Business Partner</a></h3><p>10th of Ramadan · Full time</p></article>
  <article class="job-card"><span class="tag">Operations</span><h3><a href="jobs/shift-operations-lead.html">Shift Operations Lead — Distribution</a></h3><p>Greater Cairo · Full time</p></article>
</div></section>
"@

Write-Page "news.html" "News | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="kicker">Insights</p><h1>News</h1><p class="lead">Original notes on industrial workforce topics. Not syndicated from other agencies.</p></div></section>
<section class="section"><div class="wrap grid-3">
  <article class="news-card"><p class="muted">12 Mar 2026 · Lina Farouk</p><h3><a href="news/skills-for-industry.html">Technician pipelines for expanding plants</a></h3><p>Why three-year craft academies beat last-minute overtime when a new line starts.</p></article>
  <article class="news-card"><p class="muted">02 Feb 2026 · Karim Nassar</p><h3><a href="news/workforce-planning.html">Headcount plans that survive a shutdown week</a></h3><p>A simple rolling view of absences, contractors, and critical tickets.</p></article>
</div></section>
"@

Write-Page "send-cv.html" "Send your CV | Elsewedy People" @"
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
"@

Write-Page "search.html" "Search | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="kicker">Search</p><h1>Results</h1><p class="lead">You searched for: <strong data-query>all pages</strong></p></div></section>
<section class="section"><div class="wrap">
  <p>This static demo does not run a search index. Browse services, jobs, and news from the header.</p>
  <p><a class="btn" href="jobs.html">View vacancies</a></p>
</div></section>
"@

Write-Page "privacy.html" "Privacy Policy | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><h1>Privacy policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>This demonstration website does not collect personal data on a server. Forms show an on-page confirmation only.</p>
  <p>If you later connect hosting, analytics, or an ATS, publish a full notice covering the controller, purposes, retention, and candidate rights under applicable Egyptian law.</p>
</div></section>
"@

Write-Page "cookies.html" "Cookie Policy | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><h1>Cookie policy</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>This static demo does not set tracking cookies. A future production host may use essential cookies for session security.</p>
</div></section>
"@

Write-Page "jobs/plant-hr-bp.html" "Plant HR Business Partner | Elsewedy People" @"
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
"@ $true

Write-Page "jobs/shift-operations-lead.html" "Shift Operations Lead | Elsewedy People" @"
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
"@ $true

Write-Page "news/skills-for-industry.html" "Technician pipelines | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="muted">12 Mar 2026 · Lina Farouk</p><h1>Technician pipelines for expanding plants</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>When a new line is announced, overtime hides the real gap for about six weeks. After that, quality and safety start to show the missing craft skills.</p>
  <p>A workable pipeline names the three craft families the plant cannot borrow from contractors, funds a shared workshop with a technical school, and puts a supervisor in the room every Friday.</p>
  <p><a href="../news.html">Back to news</a></p>
</div></section>
"@ $true

Write-Page "news/workforce-planning.html" "Workforce planning | Elsewedy People" @"
<section class="page-hero"><div class="wrap"><p class="muted">02 Feb 2026 · Karim Nassar</p><h1>Headcount plans that survive a shutdown week</h1></div></section>
<section class="section"><div class="wrap prose">
  <p>Annual headcount files go stale the first time a furnace trips. A living plan tracks three numbers weekly: people at work, people absent, and tickets that only a named craft can close.</p>
  <p>We keep that view with plant HR so outsourcing top-ups are a decision, not a surprise invoice.</p>
  <p><a href="../news.html">Back to news</a></p>
</div></section>
"@ $true

Write-Output "done"
