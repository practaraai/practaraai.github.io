/* Practara AI instant website scorecard. Scans via the Apps Script web app (doGet?action=scan). */
(function(){
var CFG=window.PRACTARA||{}, LOCAL=/^(localhost|127\.0\.0\.1)$/.test(location.hostname);
var SCAN=LOCAL?"/scan":CFG.endpoint, LEAD=LOCAL?"/lead":CFG.endpoint;
var form=document.getElementById("scan-form"), out=document.getElementById("scan-result");
if(!form||!out)return;
var last=null;
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
function color(s){return s>=80?"#2BB3A3":s>=60?"#3B3F99":"#b4472e";}
function render(r){
 last=r;
 var rows=r.checks.map(function(c){var st=c.pass?"pass":c.partial?"part":"fail";
  return '<li class="ck '+st+'"><span class="dot" aria-hidden="true"></span><span class="ck-l">'+esc(c.label)+'</span><span class="ck-d">'+esc(c.detail)+'</span><span class="sr">'+(c.pass?"Passed":c.partial?"Needs work":"Missing")+'</span></li>';}).join("");
 var issues=r.issues.length?r.issues.map(function(i){return "<li>"+esc(i)+"</li>";}).join(""):"<li>Your basics look strong. The deeper audit shows where competitors and AI answers still beat you.</li>";
 var psi=(r.pagespeed!=null)?'<p class="small">Google mobile speed score: <strong>'+r.pagespeed+' of 100</strong></p>':"";
 out.innerHTML='<div class="scorecard" tabindex="-1" id="scorecard">'+
 '<div class="sc-head"><div class="sc-ring" style="--p:'+r.score+';--c:'+color(r.score)+'"><span><b>'+r.score+'</b><small>of 100</small></span></div>'+
 '<div><p class="eyebrow">Instant website scorecard</p><h2>Grade '+esc(r.grade)+' for '+esc(r.url.replace(/^https?:\/\//,"").replace(/\/$/,""))+'</h2>'+psi+
 '<p class="small">An automated check of your homepage only. Your full audit is reviewed by a person.</p></div></div>'+
 '<h3>Top things holding your website back</h3><ol class="issues">'+issues+'</ol>'+
 '<details class="all"><summary>See all 13 checks</summary><ul class="cks">'+rows+'</ul></details>'+
 '<div class="tease"><h3>What this quick scan cannot see</h3><ul class="checks"><li><strong>AI search visibility:</strong> whether ChatGPT, Google AI, and Perplexity name your practice for your key procedures</li><li><strong>Competitors:</strong> which local practices win the patients searching for what you do, and why</li><li><strong>Insurance and patient mix:</strong> whether your site attracts the patients and plans you serve best</li></ul></div>'+
 '</div>'+leadForm(r);
 wireLead();
 var tpl=document.getElementById("fd-plans-tpl");
 if(tpl&&tpl.content){out.appendChild(tpl.content.cloneNode(true));}
 var sc=document.getElementById("scorecard");sc.focus({preventScroll:true});sc.scrollIntoView({behavior:"smooth",block:"start"});
}
function leadForm(r){
 return '<div class="card lead-card" id="lead"><h2>Get your free deeper analysis and a 30-minute call</h2>'+
 '<p>We will review your full site, AI answers, and local competitors, then walk you through the results on a short call. No cost, no pressure.</p>'+
 '<p class="notice" role="note"><strong>Please do not include patient information.</strong></p>'+
 '<form id="lead-form" novalidate>'+
 '<div class="grid2"><div><label for="l-name">Your name</label><input id="l-name" name="contact" autocomplete="name" maxlength="200" required></div>'+
 '<div><label for="l-org">Practice name</label><input id="l-org" name="practice" autocomplete="organization" maxlength="200" required></div>'+
 '<div><label for="l-email">Work email</label><input id="l-email" name="email" type="email" autocomplete="email" maxlength="200" required></div>'+
 '<div><label for="l-phone">Phone</label><input id="l-phone" name="phone" type="tel" autocomplete="tel" maxlength="50" required></div></div>'+
 '<div class="grid2"><div><label for="l-city">Practice city</label><input id="l-city" name="city" autocomplete="address-level2" maxlength="100" required></div><div><label for="l-state">Practice state</label><select id="l-state" name="state" required><option value="">Choose a state</option><option value="AL">Alabama</option><option value="AK">Alaska</option><option value="AZ">Arizona</option><option value="AR">Arkansas</option><option value="CA">California</option><option value="CO">Colorado</option><option value="CT">Connecticut</option><option value="DE">Delaware</option><option value="DC">District of Columbia</option><option value="FL">Florida</option><option value="GA">Georgia</option><option value="HI">Hawaii</option><option value="ID">Idaho</option><option value="IL">Illinois</option><option value="IN">Indiana</option><option value="IA">Iowa</option><option value="KS">Kansas</option><option value="KY">Kentucky</option><option value="LA">Louisiana</option><option value="ME">Maine</option><option value="MD">Maryland</option><option value="MA">Massachusetts</option><option value="MI">Michigan</option><option value="MN">Minnesota</option><option value="MS">Mississippi</option><option value="MO">Missouri</option><option value="MT">Montana</option><option value="NE">Nebraska</option><option value="NV">Nevada</option><option value="NH">New Hampshire</option><option value="NJ">New Jersey</option><option value="NM">New Mexico</option><option value="NY">New York</option><option value="NC">North Carolina</option><option value="ND">North Dakota</option><option value="OH">Ohio</option><option value="OK">Oklahoma</option><option value="OR">Oregon</option><option value="PA">Pennsylvania</option><option value="PR">Puerto Rico</option><option value="RI">Rhode Island</option><option value="SC">South Carolina</option><option value="SD">South Dakota</option><option value="TN">Tennessee</option><option value="TX">Texas</option><option value="UT">Utah</option><option value="VT">Vermont</option><option value="VA">Virginia</option><option value="WA">Washington</option><option value="WV">West Virginia</option><option value="WI">Wisconsin</option><option value="WY">Wyoming</option></select></div><div>'+
 '<label for="l-time">Best time for a call</label><select id="l-time" name="best_time"><option>Weekday morning</option><option>Weekday midday</option><option>Weekday afternoon</option><option>Any time</option></select></div></div>'+
 '<div aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden"><label for="l-hp">Leave this empty</label><input id="l-hp" name="company_website" tabindex="-1" autocomplete="off"></div>'+
 '<input type="hidden" name="website" value="'+esc(r.url)+'"><input type="hidden" name="score" value="'+r.score+'"><input type="hidden" name="grade" value="'+esc(r.grade)+'"><input type="hidden" name="source" value="scorecard">'+
 '<input type="hidden" name="type" value=""><input type="hidden" name="message" value="Instant scorecard lead"><input type="hidden" name="ref" value="'+esc(new URLSearchParams(location.search).get("ref")||location.pathname)+'">'+
 '<button class="btn" type="submit">Book my free deeper analysis</button><p id="lead-error" class="small" role="alert" hidden></p></form>'+
 '<div id="lead-thanks" role="status" hidden><h3>Request received.</h3><p>Thank you. Grab a 30-minute call time now, and we will share your deeper analysis on the call.</p><p><a class="btn" href="https://calendly.com/practara-ai/30min" target="_blank" rel="noopener">Pick a time on my calendar</a></p></div>'+
 '<p class="small">Prefer email? Write to <a href="mailto:'+CFG.email+'">'+CFG.email+'</a>.</p></div>';
}
function wireLead(){
 var f=document.getElementById("lead-form");
 f.addEventListener("submit",function(e){
  e.preventDefault();var err=document.getElementById("lead-error");
  if(!f.checkValidity()){err.textContent="Please fill in your name, practice, a valid email, phone, city and state.";err.hidden=false;f.reportValidity();return;}
  err.hidden=true;
  var done=function(){f.hidden=true;document.getElementById("lead-thanks").hidden=false;};
  if(f.company_website.value){done();return;}
  var b=f.querySelector("button");b.disabled=true;b.textContent="Sending...";
  fetch(LEAD,{method:"POST",mode:LOCAL?"same-origin":"no-cors",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams(new FormData(f)).toString()})
  .then(done).catch(function(){
   var body="";new FormData(f).forEach(function(v,k){if(k!=="company_website"&&v)body+=k+": "+v+"\n";});
   location.href="mailto:"+CFG.email+"?subject="+encodeURIComponent("Deeper analysis request")+"&body="+encodeURIComponent(body);done();});
 });
}
function run(url){
 var btn=form.querySelector("button"),msg=document.getElementById("scan-msg");
 url=(url||"").trim();
 if(!url||!/^(https?:\/\/)?[a-z0-9.-]+\.[a-z]{2,}(\/.*)?$/i.test(url)){msg.textContent="Please enter your website address, like yourpractice.com.";msg.hidden=false;return;}
 msg.hidden=true;btn.disabled=true;btn.textContent="Scanning...";
 out.innerHTML='<div class="scanning" role="status"><span class="spin" aria-hidden="true"></span>Checking your homepage, mobile setup, Google basics, and AI access. This takes about 15 to 30 seconds.</div>';
 fetch(SCAN+(SCAN.indexOf("?")<0?"?":"&")+"action=scan&url="+encodeURIComponent(url))
 .then(function(r){return r.json();})
 .then(function(r){if(!r.ok)throw new Error(r.error||"Scan failed");render(r);})
 .catch(function(e){out.innerHTML='<div class="card"><p role="alert"><strong>We could not scan that site automatically.</strong> '+esc(e.message&&e.message.indexOf("valid")>=0?e.message:"Some sites block automated checks.")+' You can still <a href="audit.html?url='+encodeURIComponent(url)+'#request">request a free audit</a> and a person will review it.</p></div>';})
 .then(function(){btn.disabled=false;btn.textContent="Get my free score";});
}
form.addEventListener("submit",function(e){e.preventDefault();run(form.url.value);});
var q=new URLSearchParams(location.search).get("scan");if(q){form.url.value=q.slice(0,300);run(q);}
})();
