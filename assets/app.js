(function(){
  "use strict";
  /* ---------- Mobile drawer ---------- */
  var toggle=document.getElementById('navToggle');
  var drawer=document.getElementById('drawer');
  var backdrop=document.getElementById('drawerBackdrop');
  var closeBtn=document.getElementById('drawerClose');
  var lastFocus=null;
  function openDrawer(){
    lastFocus=document.activeElement;
    drawer.classList.add('open');backdrop.classList.add('open');
    drawer.setAttribute('aria-hidden','false');toggle.setAttribute('aria-expanded','true');
    closeBtn.focus();
  }
  function closeDrawer(){
    drawer.classList.remove('open');backdrop.classList.remove('open');
    drawer.setAttribute('aria-hidden','true');toggle.setAttribute('aria-expanded','false');
    if(lastFocus)lastFocus.focus();
  }
  toggle.addEventListener('click',openDrawer);
  closeBtn.addEventListener('click',closeDrawer);
  backdrop.addEventListener('click',closeDrawer);
  drawer.addEventListener('click',function(e){if(e.target.tagName==='A')closeDrawer();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&drawer.classList.contains('open'))closeDrawer();});

  /* ---------- Header brands dropdown (desktop) ---------- */
  var drop=document.getElementById('brandsDrop');
  if(drop){
    var dToggle=drop.querySelector('.nav-drop-toggle');
    var openDrop=function(){drop.classList.add('open');dToggle.setAttribute('aria-expanded','true');};
    var closeDrop=function(){drop.classList.remove('open');dToggle.setAttribute('aria-expanded','false');};
    dToggle.addEventListener('click',function(e){
      e.preventDefault();
      (drop.classList.contains('open')?closeDrop:openDrop)();
    });
    document.addEventListener('click',function(e){if(!drop.contains(e.target))closeDrop();});
    drop.addEventListener('keydown',function(e){if(e.key==='Escape'){closeDrop();dToggle.focus();}});
    [].slice.call(drop.querySelectorAll('.nav-dropdown a')).forEach(function(a){
      a.addEventListener('click',closeDrop);
    });
  }

  /* ---------- Sticky CTA bar (mobile) ---------- */
  var bar=document.getElementById('stickyBar');
  var dismiss=document.getElementById('stickyDismiss');
  var heroCTA=document.querySelector('.hero .btn--primary');
  var finalCTA=document.getElementById('final-cta');
  var dismissed=false;
  try{dismissed=sessionStorage.getItem('mct_sticky_dismissed')==='1';}catch(e){}
  var heroVisible=true, finalVisible=false;
  function update(){
    var show=!dismissed && !heroVisible && !finalVisible;
    bar.classList.toggle('show',show);
    bar.setAttribute('aria-hidden',show?'false':'true');
    var focusables=bar.querySelectorAll('a,button');
    focusables.forEach(function(el){el.tabIndex=show?0:-1;});
  }
  if('IntersectionObserver'in window){
    if(heroCTA){new IntersectionObserver(function(en){heroVisible=en[0].isIntersecting;update();}).observe(heroCTA);}
    if(finalCTA){new IntersectionObserver(function(en){finalVisible=en[0].isIntersecting;update();},{rootMargin:'0px 0px -10% 0px'}).observe(finalCTA);}
  }
  dismiss.addEventListener('click',function(){
    dismissed=true;try{sessionStorage.setItem('mct_sticky_dismissed','1');}catch(e){}
    update();
  });
  update();

  /* ---------- Scroll reveal + on-view animations ---------- */
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revealEls=[].slice.call(document.querySelectorAll('.reveal'));
  if(reduce||!('IntersectionObserver'in window)){
    revealEls.forEach(function(el){el.classList.add('in-view');});
  }else{
    var ro=new IntersectionObserver(function(ents){
      ents.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in-view');ro.unobserve(e.target);}});
    },{rootMargin:'0px 0px -8% 0px',threshold:0.08});
    revealEls.forEach(function(el){ro.observe(el);});
  }

  /* ---------- Field checklist progress (multiple, persisted locally) ---------- */
  var checklists=[].slice.call(document.querySelectorAll('[data-checklist]'));
  checklists.forEach(function(clt){
    var checks=[].slice.call(clt.querySelectorAll('.cl-check'));
    if(!checks.length)return;
    var fill=clt.querySelector('[data-cl-fill]');
    var countEl=clt.querySelector('[data-cl-count]');
    var pbar=clt.querySelector('.cl-progress');
    var total=checks.length;
    var name=clt.getAttribute('data-checklist')||'';
    var key=name?('mct_cl_'+name):null;
    /* restore prior ticks from this device only — no account, no email */
    if(key){
      try{
        var saved=JSON.parse(localStorage.getItem(key)||'[]');
        if(saved&&saved.length){checks.forEach(function(c,i){if(saved.indexOf(i)>-1)c.checked=true;});}
      }catch(e){}
    }
    var upd=function(){
      var n=0,on=[];
      checks.forEach(function(c,i){if(c.checked){n++;on.push(i);}});
      if(countEl)countEl.textContent=n;
      if(fill)fill.style.width=(total?n/total*100:0)+'%';
      if(pbar)pbar.setAttribute('aria-valuenow',n);
      if(key){try{localStorage.setItem(key,JSON.stringify(on));}catch(e){}}
    };
    checks.forEach(function(c){c.addEventListener('change',upd);});
    upd();
  });

  /* ---------- Save / print checklist (no email capture) ---------- */
  [].slice.call(document.querySelectorAll('[data-print]')).forEach(function(b){
    b.addEventListener('click',function(e){e.preventDefault();window.print();});
  });

  /* ---------- Fit Map: bidirectional list <-> diagram highlight ---------- */
  var fmWrap=document.querySelector('.fm-interactive');
  if(fmWrap){
    var fmPoints=[].slice.call(fmWrap.querySelectorAll('.fm-point'));
    var fmNotes=[].slice.call(fmWrap.querySelectorAll('[data-fm].fm-note'));
    var fmSet=function(id,on){
      fmPoints.forEach(function(p){if(p.getAttribute('data-fm')===id)p.classList.toggle('is-active',on);});
      fmNotes.forEach(function(n){if(n.getAttribute('data-fm')===id)n.classList.toggle('is-active',on);});
    };
    var fmBind=function(el){
      var id=el.getAttribute('data-fm');
      el.addEventListener('mouseenter',function(){fmSet(id,true);});
      el.addEventListener('mouseleave',function(){fmSet(id,false);});
      el.addEventListener('focus',function(){fmSet(id,true);});
      el.addEventListener('blur',function(){fmSet(id,false);});
    };
    fmPoints.forEach(fmBind);
    fmNotes.forEach(function(n){n.style.cursor='pointer';fmBind(n);});
  }

  /* ---------- Section nav: mark the section in view ---------- */
  var tocLinks=[].slice.call(document.querySelectorAll('[data-toc] a'));
  if(tocLinks.length&&'IntersectionObserver'in window){
    var byId={};
    tocLinks.forEach(function(a){byId[a.getAttribute('href').slice(1)]=a;});
    var sections=tocLinks.map(function(a){return document.getElementById(a.getAttribute('href').slice(1));}).filter(Boolean);
    var tobs=new IntersectionObserver(function(ents){
      ents.forEach(function(en){
        var a=byId[en.target.id];
        if(!a)return;
        if(en.isIntersecting){
          tocLinks.forEach(function(l){l.removeAttribute('aria-current');});
          a.setAttribute('aria-current','true');
        }
      });
    },{rootMargin:'-120px 0px -70% 0px',threshold:0});
    sections.forEach(function(s){tobs.observe(s);});
  }

  /* ---------- Retailer outbound-click tracking (GA4, delegated) ---------- */
  /* Fires a `retailer_outbound_click` event when a reader follows a disclosed
     retailer-example link. Links opt in via data-retailer="mcm|hcm"; the other
     parameters are read from data-* attributes so no per-link JS is needed. */
  document.addEventListener('click',function(e){
    var a=e.target.closest?e.target.closest('a[data-retailer]'):null;
    if(!a||typeof window.gtag!=='function')return;
    try{
      window.gtag('event','retailer_outbound_click',{
        retailer:a.getAttribute('data-retailer')||'',
        source_page:location.pathname,
        destination_url:a.href,
        intent_cluster:a.getAttribute('data-intent')||'',
        brand:a.getAttribute('data-brand')||'',
        location:a.getAttribute('data-location')||'',
        anchor_text:(a.textContent||'').replace(/\s+/g,' ').trim().slice(0,120)
      });
    }catch(err){}
  });
})();
