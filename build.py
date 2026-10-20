# Generator for the Practara AI static site. Run: python3 build.py
import json, os
D="https://practaraai.github.io"
EMAIL="practara.ai@gmail.com"
# Google Apps Script web app URL (ends in /exec). Empty = form falls back to email.
FORM_ENDPOINT="https://script.google.com/macros/s/AKfycbyors1TR2mlBP-3cODe-wrb-KfAj4UwGcuQu2Fs3e7EpnobTQHd3bq_HpzmT4oYQN9-/exec"
NAV=[("index.html","Home"),("services.html","Services"),("pricing.html","Pricing"),("about.html","About"),("audit.html","Free audit")]
LD={"@context":"https://schema.org","@type":["Organization","ProfessionalService"],"name":"Practara AI","url":D+"/","logo":D+"/favicon.svg","description":"Website rebuilds plus AI search and SEO visibility, brand, and analytics for ambulatory surgery centers and physician practices.","areaServed":{"@type":"Country","name":"United States"},"email":EMAIL,"knowsAbout":["Medical practice websites","Ambulatory surgery center marketing","AI search visibility","Healthcare SEO","Privacy-conscious web analytics"]}
def page(fn,title,desc,body,extra=""):
    nav="".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fn else ""}{" class=\"btn btn-sm\"" if h=="audit.html" else ""}>{t}</a>' for h,t in NAV)
    can=D+"/"+("" if fn=="index.html" else fn)
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Practara AI">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{can}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#3B3F99">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap bar">
<a class="brand" href="index.html" aria-label="Practara AI home"><img src="logo.svg" alt="Practara AI" width="168" height="36"></a>
<nav aria-label="Main">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap foot">
<p><strong>Practara AI</strong> | Help patients and AI understand your practice.<br>Websites and AI search visibility for ambulatory surgery centers and physician practices. Serving clients across the United States.</p>
<p><a href="services.html">Services</a> · <a href="pricing.html">Pricing</a> · <a href="about.html">About</a> · <a href="audit.html">Free audit</a> · <a href="privacy.html">Privacy</a></p>
<p class="small">&copy; 2026 Practara AI.</p>
</div></footer>
</body>
</html>
'''
    assert "\u2014" not in html and "\u2013" not in html
    open(fn,"w").write(html)
SCAN_BOX='<form id="scan-form" class="scan-box" novalidate aria-label="Free website score"><label for="scan-url">Enter your practice website for a free instant score</label><input id="scan-url" name="url" type="text" inputmode="url" autocomplete="url" placeholder="yourpractice.com" maxlength="300" required><button class="btn" type="submit">Get my free score</button><p id="scan-msg" class="small" role="alert" hidden></p></form>'
SCAN_OUT='<section class="wrap scan-wrap" aria-live="polite"><div id="scan-result"></div></section>'
SCAN_JS=f'<script>window.PRACTARA={json.dumps({"endpoint":FORM_ENDPOINT,"email":EMAIL})};</script><script src="scorecard.js" defer></script>'
cta='<section class="cta"><div class="wrap"><h2>See what your website says about your care.</h2><p>Request a free website audit. No signup, no patient information.</p><div class="actions cta-actions"><a class="btn btn-light" href="audit.html">Request your free audit</a><a class="btn btn-light" href="https://calendly.com/practara-ai/30min" target="_blank" rel="noopener">Book a 30-minute call</a></div></div></section>'
FAQ_AI='<details><summary>Do you offer AI tools for patient intake or follow-up?</summary><p>No. We build and maintain your website and its search and AI visibility.</p></details>'
ld=f'<script type="application/ld+json">{json.dumps(LD)}</script>\n'

page("index.html","Practara AI | Websites and AI visibility for surgery centers and physician practices",
"Your care has advanced. See if your website shows it. Practara AI rebuilds websites for surgery centers and physician practices. Request a free website audit.",
f'''<section class="hero"><div class="wrap">
<p class="eyebrow">Help patients and AI understand your practice.</p>
<h1>Your care has advanced. Your website hasn't.</h1>
<p class="lead">Your procedures, technology, and physician training have moved forward. Practara AI rebuilds websites for surgery centers and physician practices so patients, referring physicians, Google, and AI assistants can see that clearly.</p>
{SCAN_BOX}
<p class="small">Free, instant, and no signup. We only check your public website. The instant score is automated; your full audit is generated with automated tools and reviewed by a person. Your website address and score are saved (see <a href="privacy.html">Privacy</a>). Please do not include patient information. <a href="pricing.html">See pricing</a></p>
</div></section>
{SCAN_OUT}
<section class="wrap section"><h2>Patients judge your care by your website before they meet you</h2>
<p class="intro">When a website looks dated, patients and referring physicians may assume the care is dated too. Your care may be far more current than your site shows. Patients cannot see your operating rooms, your equipment, or your physicians' training. They see your homepage.</p>
<div class="grid3">
<article class="card"><h3>Patients may choose another practice</h3><p>If your site is slow on a phone or unclear, a patient can tap back and pick the next result. AI assistants have little to go on when your pages are thin or unclear.</p></article>
<article class="card"><h3>The wrong patient mix</h3><p>Without clear insurance information, self-pay details where you choose to publish them, and pages for the procedures you focus on, the patients you serve best have a harder time finding you.</p></article>
<article class="card"><h3>An outdated site</h3><p>Procedures are hard to find, technology goes unmentioned, and board certifications, fellowships, and specialties are missing or out of date.</p></article>
</div></section>
<section class="band"><div class="wrap section split">
<div><h2>Built by someone who has worked in medicine</h2><p>Practara AI's founder has 5 years of experience in the medical field. That is why we start with your procedures, your physicians, and your patients, and then build the website around them. Insiders who understand providers, not a generic tech company.</p><a href="about.html">More about us</a></div>
<ul class="checks"><li>No patient health information in standard web forms or analytics</li><li>No ad pixels or session replay on clinical pages</li><li>Content your clinical team reviews and approves before anything goes live</li><li>Accessibility designed to target WCAG 2.2 AA</li><li>No guarantees of rankings, AI answers, or patient volume. We fix what makes your site harder to understand and report on what changes.</li></ul>
</div></section>
<section class="wrap section"><h2>How it works</h2>
<ol class="steps"><li><strong>Get your instant score.</strong> Enter your website above and see what is holding it back.</li><li><strong>Request your free deeper analysis.</strong> We review AI search visibility, competitors, and your insurance patient mix.</li><li><strong>Review pricing.</strong> Website and AI Visibility plan: $2,500 per quarter, or $1,000 per quarter for our first 5 Founding Clients. 12-month contract, $0 down.</li><li><strong>Book a free 30-minute call.</strong> We walk through your results and what we would fix first. No pressure.</li><li><strong>Get a written proposal.</strong> A clear scope, price, and timeline.</li></ol>
</section>
{cta}{SCAN_JS}''',ld)

page("services.html","Services | Practara AI","Website rebuilds, AI search visibility, SEO, brand, and privacy-safe analytics for ambulatory surgery centers and physician practices.",
f'''<section class="hero hero-sm"><div class="wrap"><h1>Services</h1><p class="lead">A modern practice website plus AI visibility, built for surgery centers and independent physician practices.</p></div></section>
<section class="wrap section"><div class="grid2">
<article class="card"><h2>Website rebuild</h2><p>Modern, mobile-first, fast, and accessible (WCAG 2.2 AA target). Pages for procedures, physicians, locations, patient prep and FAQs, insurance and pricing transparency, and careers.</p></article>
<article class="card"><h2>AI search visibility</h2><p>Medical schema, clear facts about who you are and what you do, quotable FAQ content, llms.txt, AI crawler access, and consistent listings across Google Business Profile, Healthgrades, Vitals, and NPPES.</p></article>
<article class="card"><h2>SEO strategy</h2><p>Procedure and city pages, physician bio pages, referral-source pages, and technical SEO.</p></article>
<article class="card"><h2>Procedure and technology pages</h2><p>One page per key procedure and per device or technique you actually use: what it is, who it suits, what recovery looks like, and your real experience with it.</p></article>
<article class="card"><h2>Physician credential profiles</h2><p>Board certifications that name the certifying board, fellowships, residencies, publications, and procedure focus, sourced from the physician's own CV and approved by the physician.</p></article>
<article class="card"><h2>Right-patient pages</h2><p>Accepted plans, self-pay information where you choose to publish it, and pages that help the patients you serve best find you.</p></article>
<article class="card"><h2>Brand refresh</h2><p>Logo cleanup, a color and type system, photography guidance, and consistent naming across listings.</p></article>
<article class="card"><h2>Privacy-safe analytics</h2><p>No tracking of health-condition pages to ad platforms. Call and form-start tracking, and a monthly report with your AI visibility score history.</p></article>
</div></section>
<section class="band"><div class="wrap section"><h2>Privacy-conscious by design</h2><p>Standard contact forms collect only name, phone, email, and a general question. Appointment requests and intake link to your existing patient portal, so patient health information does not pass through your marketing site.</p></div></section>
{cta}''')

page("pricing.html","Pricing | Practara AI","One plan: $2,500 per quarter on a 12-month contract with $0 down. Founding Client offer: first 5 clients at $1,000 per quarter.",
f'''<section class="hero hero-sm"><div class="wrap"><h1>One plan. Simple, upfront pricing.</h1><p class="lead">Clear facts. Modern website. Your practice.</p></div></section>
<section class="wrap section"><div class="grid2 pricing">
<article class="card price"><h2>Practara Plan</h2><p class="amount">$2,500 <span>per quarter</span></p><p>12-month contract. $0 down.</p>
<ul class="checks"><li>Modern, mobile-first website rebuild designed to target WCAG 2.2 AA</li><li>Procedure, technology, and physician training pages, approved by your clinical team</li><li>Self-pay pricing and insurance information pages, where you choose to publish them</li><li>AI search visibility: medical structured data, llms.txt, clear entity facts, consistent listings</li><li>SEO: procedure, location, and physician pages plus technical fixes</li><li>Brand cleanup: logo, colors, type, photography guidance</li><li>Privacy-conscious forms that collect contact details only, with appointment requests linked to your patient portal</li><li>Privacy-safe analytics and a simple monthly report</li><li>Hosting, security, and updates</li></ul>
<a class="btn" href="audit.html">Start with a free audit</a></article>
<article class="card price featured"><p class="tag">Founding Client offer: 5 spots</p><h2>Founding Client</h2><p class="amount">$1,000 <span>per quarter</span></p><p>The full Practara Plan for our first 5 clients, on the same 12-month contract with $0 down.</p>
<p><strong>In exchange, Founding Clients agree to:</strong></p><ul class="checks"><li>A case study about the project</li><li>Use of their practice logo on our website</li><li>A written testimonial from the practice owner or a physician about working with Practara AI (a business endorsement, never a patient story)</li><li>Beta access: trying new features early and giving feedback</li></ul>
<a class="btn" href="audit.html">Ask about a founding spot</a></article>
</div>
<p class="small center">Disclosure: Founding Clients receive discounted pricing in exchange for a case study, logo use, a testimonial, and beta feedback. Final scope is confirmed in a written agreement. Prices in US dollars.</p></section>
<section class="band"><div class="wrap section"><h2>Questions</h2>
<details><summary>Is there a setup fee?</summary><p>No. The plan is $0 down and billed quarterly.</p></details>
<details><summary>Can you guarantee we will rank first on Google or appear in ChatGPT?</summary><p>No. No one can honestly guarantee search rankings, AI answers, or patient volume. We fix what makes your site harder for people, search engines, and AI tools to understand, and we report on what changes.</p></details>
{FAQ_AI}
<details><summary>We already have a web vendor. Is this still useful?</summary><p>Yes. Many teams share their audit results with their current vendor as a to-do list.</p></details>
</div></section>
{cta}''')

page("about.html","About | Practara AI","Practara AI was founded on the West Coast after 5 years in the medical field. We help surgery centers and practices show patients what they actually do.",
f'''<section class="hero hero-sm"><div class="wrap"><h1>About Practara AI</h1><p class="lead">Built by someone who has worked inside healthcare.</p></div></section>
<section class="wrap section prose">
<h2>Why we exist</h2><p>Many physicians are excellent. They use advanced technology, modern procedures, and refined techniques, and they have serious training. Their websites show almost none of it. Patients cannot see what makes the practice good, so they book somewhere that looks more current.</p>
<p>Most practices do not know what they do not know about marketing: who their right patient is, where those patients go instead, and why they pick a competitor. We find the gap between how good the practice really is and what its website and AI answers say, then close it.</p>
<h2>Our founder</h2><p>Practara AI was founded on the West Coast after 5 years in the medical field. We work with ambulatory surgery centers and physician practices across the United States.</p>
<h2>How we work</h2><ul class="checks"><li>No claims we cannot substantiate, and no guarantees of results</li><li>"Board certified" always names the board</li><li>Patient stories only with the patient's written permission</li><li>Your practice approves every page before it publishes</li></ul>

</section>
{cta}''')

AUDIT_FORM=("""<form id="audit-form" novalidate>
<label for="org">Practice name</label><input id="org" name="practice" autocomplete="organization" maxlength="500" required>
<label for="name">Contact name</label><input id="name" name="contact" autocomplete="name" maxlength="500" required>
<label for="email">Work email</label><input id="email" name="email" type="email" autocomplete="email" maxlength="500" required>
<label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel" maxlength="500">
<label for="site">Website URL</label><input id="site" name="website" type="url" inputmode="url" placeholder="https://" maxlength="500" required>
<label for="city">Practice city</label><input id="city" name="city" autocomplete="address-level2" maxlength="100" required>
<label for="state">Practice state</label><select id="state" name="state" required><option value="">Choose a state</option><option value="AL">Alabama</option><option value="AK">Alaska</option><option value="AZ">Arizona</option><option value="AR">Arkansas</option><option value="CA">California</option><option value="CO">Colorado</option><option value="CT">Connecticut</option><option value="DE">Delaware</option><option value="DC">District of Columbia</option><option value="FL">Florida</option><option value="GA">Georgia</option><option value="HI">Hawaii</option><option value="ID">Idaho</option><option value="IL">Illinois</option><option value="IN">Indiana</option><option value="IA">Iowa</option><option value="KS">Kansas</option><option value="KY">Kentucky</option><option value="LA">Louisiana</option><option value="ME">Maine</option><option value="MD">Maryland</option><option value="MA">Massachusetts</option><option value="MI">Michigan</option><option value="MN">Minnesota</option><option value="MS">Mississippi</option><option value="MO">Missouri</option><option value="MT">Montana</option><option value="NE">Nebraska</option><option value="NV">Nevada</option><option value="NH">New Hampshire</option><option value="NJ">New Jersey</option><option value="NM">New Mexico</option><option value="NY">New York</option><option value="NC">North Carolina</option><option value="ND">North Dakota</option><option value="OH">Ohio</option><option value="OK">Oklahoma</option><option value="OR">Oregon</option><option value="PA">Pennsylvania</option><option value="PR">Puerto Rico</option><option value="RI">Rhode Island</option><option value="SC">South Carolina</option><option value="SD">South Dakota</option><option value="TN">Tennessee</option><option value="TX">Texas</option><option value="UT">Utah</option><option value="VT">Vermont</option><option value="VA">Virginia</option><option value="WA">Washington</option><option value="WV">West Virginia</option><option value="WI">Wisconsin</option><option value="WY">Wyoming</option></select>
<label for="type">Practice type</label><select id="type" name="type"><option value="">Choose one</option><option>Ambulatory surgery center</option><option>Physician practice</option><option>Multi-specialty group</option><option>Other</option></select>
<label for="msg">Message (optional)</label><textarea id="msg" name="message" rows="3" maxlength="500" aria-describedby="msg-help"></textarea>
<p id="msg-help" class="small">Please do not include patient information.</p>
<div aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden"><label for="hp">Leave this empty</label><input id="hp" name="company_website" tabindex="-1" autocomplete="off"></div>
<input type="hidden" id="ref" name="ref">
<button class="btn" type="submit">Send audit request</button>
<p id="form-error" class="small" role="alert" hidden></p>
</form>
<div id="form-thanks" role="status" hidden><h3>Thank you.</h3><p>We received your request. Book a 30-minute call to go over your results.</p><p><a class="btn" href="https://calendly.com/practara-ai/30min" target="_blank" rel="noopener">Pick a time on my calendar</a></p></div>
<p class="small">Prefer to write directly? Email <a href="mailto:EMAIL_X?subject=Free%20website%20audit%20request">EMAIL_X</a>.</p>
<script>
(function(){
var ENDPOINT=ENDPOINT_X, EMAIL="EMAIL_X";
var f=document.getElementById("audit-form"), q=new URLSearchParams(location.search);
if(q.get("url"))f.website.value=q.get("url").slice(0,500);
if(q.get("ref"))f.ref.value=q.get("ref").slice(0,500);
function mailto(){
 var b="";["practice","contact","email","phone","website","city","state","type","message","ref"].forEach(function(k){if(f[k].value)b+=k+": "+f[k].value+"\\n";});
 location.href="mailto:"+EMAIL+"?subject="+encodeURIComponent("Free website audit request")+"&body="+encodeURIComponent(b);
}
function thanks(){f.hidden=true;document.getElementById("form-thanks").hidden=false;}
f.addEventListener("submit",function(e){
 e.preventDefault();
 var err=document.getElementById("form-error");
 if(!f.checkValidity()){err.textContent="Please fill in the required fields, including a valid email, website URL, city and state.";err.hidden=false;f.reportValidity();return;}
 err.hidden=true;
 if(f.company_website.value){thanks();return;}
 if(!ENDPOINT){mailto();thanks();return;}
 var btn=f.querySelector("button");btn.disabled=true;btn.textContent="Sending...";
 fetch(ENDPOINT,{method:"POST",mode:"no-cors",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams(new FormData(f)).toString()})
 .then(thanks).catch(function(){mailto();thanks();});
});
})();
</script>""".replace("EMAIL_X",EMAIL).replace("ENDPOINT_X",json.dumps(FORM_ENDPOINT)))

page("audit.html","Free website audit | Practara AI","Request a free Website and AI Visibility Audit for your surgery center or physician practice.",
f'''<section class="hero hero-sm"><div class="wrap"><h1>Free website audit</h1><p class="lead">Find out what patients, and AI search, can and cannot see about your practice. Start with an instant score.</p>
'''+SCAN_BOX+'''<p class="small">Free and instant. We only check your public website. The instant score is automated; your full audit is generated with automated tools and reviewed by a person. Your website address and score are saved (see <a href="privacy.html">Privacy</a>). Please do not include patient information.</p></div></section>
'''+SCAN_OUT+f'''
<section class="wrap section split" id="request">
<div><h2>What we check</h2><ul class="checks">
<li><strong>Modern website:</strong> mobile layout, speed, HTTPS, broken links, stale content, page titles and descriptions</li>
<li><strong>AI visibility:</strong> AI crawler access, llms.txt, medical schema, FAQ content</li>
<li><strong>Listings:</strong> name, address, and phone consistency, Google Business Profile, Healthgrades, Vitals, NPPES</li>
<li><strong>Technology and procedure gap:</strong> what you do compared with what your site shows, cited to public sources</li>
<li><strong>Where your patients go:</strong> who ranks and gets named by AI tools for your key procedures, and why</li>
<li><strong>Privacy and tracking flags:</strong> ad pixels on patient pages, legacy tracking, forms that may collect patient information, accessibility basics (informational only)</li>
</ul></div>
<div class="card">
<h2>Or request your audit directly</h2>
<p class="notice" role="note"><strong>Please do not include patient information.</strong></p>
'''+AUDIT_FORM+f'''
</div></section>
'''+SCAN_JS)

page("privacy.html","Privacy | Practara AI","How Practara AI handles information on this website.",
f'''<section class="hero hero-sm"><div class="wrap"><h1>Privacy</h1><p class="lead">Last updated October 20, 2026.</p></div></section>
<section class="wrap section prose">
<h2>Cookies and tracking</h2><p>This website does not use cookies, analytics, or trackers.</p>
<h2>Hosting</h2><p>This site is hosted on GitHub Pages. GitHub may keep standard server logs, such as IP addresses, under the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub General Privacy Statement</a>.</p>
<h2>What we collect</h2><p>When you request an audit we collect your practice name, contact name, work email, phone, website address, practice city and state, practice type, preferred call time, any message you write, and a referral code or page name if you arrived from a link. When you use the instant score we save the website address you enter and its score, grade, load time, mobile speed score, and the top issue found. If you request a deeper analysis from your scorecard, that score and grade are saved with your request, along with a note that it came from the scorecard.</p>
<h2>How it is processed</h2><p>This information is sent to a Google Apps Script web app and stored in Practara AI's Google Sheet, so Google processes it through Google Apps Script and Google Sheets, including your IP address, under Google's terms. To score a website, our server fetches that site's public homepage, robots.txt, and sitemap, and may send the address to Google PageSpeed Insights.</p>
<h2>How we use it</h2><p>We use this information only to prepare your audit and to contact you about it. We do not sell it or use it for advertising.</p>
<h2>Retention and deletion</h2><p>We keep it for up to 24 months unless you ask us to delete it sooner. Email <a href="mailto:{EMAIL}">{EMAIL}</a> to see, correct, or delete your information.</p>
<h2>Patient information</h2><p>These forms are for practice owners and staff only. Please do not send patient information. If you are a patient, please contact your doctor's office directly.</p>
<h2>Questions</h2><p>Contact <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>''')

page("404.html","Page not found | Practara AI","This page could not be found.",
'<section class="hero hero-sm"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you are looking for has moved or does not exist.</p><div class="actions"><a class="btn" href="/">Go to the home page</a><a class="btn btn-ghost" href="/audit.html">Request a free audit</a></div></div></section>','<meta name="robots" content="noindex">\n')

open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{D}/{'' if p=='index.html' else p}</loc><lastmod>2026-10-14</lastmod></url>\n" for p in ["index.html","services.html","pricing.html","about.html","audit.html","privacy.html"])+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {D}/sitemap.xml\n")
open(".nojekyll","w").write("")
