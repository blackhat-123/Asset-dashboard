print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Asset Manager</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #f5f6f8;
    --white: #ffffff;
    --border: #e4e6ea;
    --text: #1a1d23;
    --muted: #8a909e;
    --blue: #2563eb;
    --green: #16a34a;
    --red: #dc2626;
    --yellow: #d97706;
    --green-bg: #f0fdf4;
    --red-bg: #fef2f2;
    --yellow-bg: #fffbeb;
    --blue-bg: #eff6ff;
    --shadow: 0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.04);
  }

  body { font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); font-size: 14px; }

  .layout { display: flex; min-height: 100vh; }

  /* SIDEBAR */
  .sidebar {
    width: 220px; background: var(--white); border-right: 1px solid var(--border);
    display: flex; flex-direction: column; padding: 20px 0;
    position: fixed; height: 100vh;
  }

  .logo { padding: 0 16px 20px; border-bottom: 1px solid var(--border); margin-bottom: 10px; }

  .logo-text { font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px; }

  .logo-icon {
    width: 28px; height: 28px; background: var(--blue); border-radius: 6px;
    display: flex; align-items: center; justify-content: center; font-size: 14px;
  }

  .nav-section { padding: 8px 16px 4px; font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }

  .nav-item {
    display: flex; align-items: center; gap: 10px;
    padding: 8px 10px; margin: 1px 8px; border-radius: 6px;
    cursor: pointer; color: var(--muted); font-size: 13.5px; font-weight: 500;
    transition: background 0.12s, color 0.12s;
  }
  .nav-item:hover { background: var(--bg); color: var(--text); }
  .nav-item.active { background: var(--blue-bg); color: var(--blue); }
  .nav-item .ni { font-size: 15px; }

  .sidebar-bottom { margin-top: auto; padding: 12px 8px 0; border-top: 1px solid var(--border); }

  /* MAIN */
  .main { margin-left: 220px; flex: 1; display: flex; flex-direction: column; }

  /* TOPBAR */
  .topbar {
    background: var(--white); border-bottom: 1px solid var(--border);
    padding: 0 24px; height: 54px;
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 10;
  }

  .page-title { font-size: 15px; font-weight: 600; }
  .topbar-right { display: flex; align-items: center; gap: 10px; }

  .search {
    display: flex; align-items: center; gap: 7px;
    background: var(--bg); border: 1px solid var(--border);
    border-radius: 7px; padding: 6px 12px; width: 210px;
    transition: border-color 0.15s;
  }
  .search:focus-within { border-color: var(--blue); }
  .search input { border: none; background: none; outline: none; font-family: 'DM Sans', sans-serif; font-size: 13px; color: var(--text); width: 100%; }
  .search input::placeholder { color: var(--muted); }

  .btn { padding: 7px 14px; border-radius: 7px; font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 500; cursor: pointer; border: none; transition: all 0.12s; }
  .btn-primary { background: var(--blue); color: #fff; }
  .btn-primary:hover { background: #1d4ed8; }
  .btn-outline { background: var(--white); color: var(--text); border: 1px solid var(--border); }
  .btn-outline:hover { background: var(--bg); }

  .user-btn { width: 30px; height: 30px; border-radius: 50%; background: var(--blue); color: white; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; cursor: pointer; }

  /* CONTENT */
  .content { padding: 22px 24px; }

  /* STATS */
  .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }

  .stat-card {
    background: var(--white); border: 1px solid var(--border); border-radius: 8px;
    padding: 16px 18px; box-shadow: var(--shadow);
  }

  .stat-label { font-size: 12px; color: var(--muted); font-weight: 500; margin-bottom: 8px; }
  .stat-row { display: flex; align-items: flex-end; justify-content: space-between; }
  .stat-value { font-size: 26px; font-weight: 600; line-height: 1; }
  .stat-icon { width: 34px; height: 34px; border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: 17px; }
  .stat-sub { font-size: 11.5px; color: var(--muted); margin-top: 6px; }

  /* TABLE */
  .table-card {
    background: var(--white); border: 1px solid var(--border);
    border-radius: 8px; box-shadow: var(--shadow); overflow: hidden; margin-bottom: 18px;
  }

  .table-header {
    padding: 14px 18px; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap;
  }

  .table-title { font-size: 14px; font-weight: 600; }
  .table-controls { display: flex; align-items: center; gap: 8px; }

  select {
    font-family: 'DM Sans', sans-serif; font-size: 13px; color: var(--text);
    background: var(--white); border: 1px solid var(--border);
    border-radius: 6px; padding: 6px 10px; cursor: pointer; outline: none;
    transition: border-color 0.12s;
  }
  select:focus { border-color: var(--blue); }

  table { width: 100%; border-collapse: collapse; }

  th {
    padding: 10px 16px; text-align: left; font-size: 11.5px; font-weight: 600;
    color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em;
    background: #fafbfc; border-bottom: 1px solid var(--border);
  }

  td { padding: 11px 16px; border-bottom: 1px solid var(--border); vertical-align: middle; font-size: 13.5px; }
  tr:last-child td { border-bottom: none; }
  tbody tr:hover td { background: #fafbfc; }

  .asset-id { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--blue); }

  .user-cell { display: flex; align-items: center; gap: 9px; }
  .avatar { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; flex-shrink: 0; }
  .name { font-weight: 500; font-size: 13.5px; }
  .dept-txt { font-size: 11.5px; color: var(--muted); }

  .badge { display: inline-flex; align-items: center; gap: 5px; padding: 3px 9px; border-radius: 20px; font-size: 12px; font-weight: 500; white-space: nowrap; }
  .badge-green { background: var(--green-bg); color: var(--green); }
  .badge-red { background: var(--red-bg); color: var(--red); }
  .badge-yellow { background: var(--yellow-bg); color: var(--yellow); }
  .badge-gray { background: var(--bg); color: var(--muted); }
  .dot { width: 6px; height: 6px; border-radius: 50%; }

  .text-muted { color: var(--muted); font-size: 13px; }
  .mono { font-family: 'DM Mono', monospace; font-size: 12px; }

  .view-btn {
    background: none; border: none; color: var(--blue); font-size: 13px;
    font-family: 'DM Sans', sans-serif; cursor: pointer; font-weight: 500;
    padding: 0; text-decoration: underline; text-underline-offset: 2px;
  }
  .view-btn:hover { color: #1d4ed8; }

  .empty td { text-align: center; padding: 32px; color: var(--muted); }

  /* BOTTOM */
  .bottom-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

  .panel {
    background: var(--white); border: 1px solid var(--border);
    border-radius: 8px; padding: 18px; box-shadow: var(--shadow);
  }
  .panel-title { font-size: 14px; font-weight: 600; margin-bottom: 14px; }

  .progress-row { margin-bottom: 12px; }
  .progress-row:last-child { margin-bottom: 0; }
  .progress-label { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 5px; }
  .progress-label span:last-child { color: var(--muted); font-size: 12px; }
  .progress-track { height: 5px; background: var(--border); border-radius: 3px; overflow: hidden; }
  .progress-fill { height: 100%; border-radius: 3px; transition: width 0.4s ease; }

  .alert-item { display: flex; align-items: flex-start; gap: 10px; padding: 10px 0; border-bottom: 1px solid var(--border); }
  .alert-item:last-child { border-bottom: none; padding-bottom: 0; }
  .alert-item:first-child { padding-top: 0; }
  .alert-dot { width: 7px; height: 7px; border-radius: 50%; margin-top: 5px; flex-shrink: 0; }
  .alert-title { font-size: 13.5px; font-weight: 500; margin-bottom: 2px; }
  .alert-sub { font-size: 12px; color: var(--muted); }
  .alert-time { margin-left: auto; font-size: 11.5px; color: var(--muted); white-space: nowrap; padding-top: 2px; }

  /* MODAL */
  .overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.25); z-index: 100; display: none; align-items: center; justify-content: center; }
  .overlay.open { display: flex; }

  .modal {
    background: var(--white); border-radius: 10px; padding: 22px;
    width: 450px; max-width: 95vw;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    animation: min 0.16s ease;
  }
  @keyframes min { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }

  .modal-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
  .modal-head h2 { font-size: 15px; font-weight: 600; }
  .close-btn { background: none; border: none; color: var(--muted); font-size: 18px; cursor: pointer; }
  .close-btn:hover { color: var(--text); }

  .av-banner { display: flex; align-items: center; gap: 9px; padding: 11px 14px; border-radius: 7px; font-size: 13.5px; font-weight: 500; margin-bottom: 16px; }

  .hr { height: 1px; background: var(--border); margin: 0 -22px 16px; }

  .detail-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 18px; }
  .dl { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; margin-bottom: 3px; }
  .dv { font-size: 13.5px; }

  .modal-foot { display: flex; justify-content: flex-end; gap: 8px; }

  .form-group { margin-bottom: 12px; }
  .form-label { display: block; font-size: 12px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
  .form-input { width: 100%; padding: 8px 11px; border: 1px solid var(--border); border-radius: 6px; font-family: 'DM Sans', sans-serif; font-size: 13.5px; color: var(--text); background: var(--white); outline: none; transition: border-color 0.12s; }
  .form-input:focus { border-color: var(--blue); }
</style>
</head>
<body>
<div class="layout">

  <aside class="sidebar">
    <div class="logo">
      <div class="logo-text"><div class="logo-icon">💻</div> AssetManager</div>
    </div>
    <div class="nav-section">Main</div>
    <div class="nav-item active"><span class="ni">🖥️</span> Laptops</div>
    <div class="nav-item"><span class="ni">👥</span> Users</div>
    <div class="nav-item"><span class="ni">🛡️</span> Security</div>
    <div class="nav-item"><span class="ni">📊</span> Reports</div>
    <div class="nav-section" style="margin-top:8px">System</div>
    <div class="nav-item"><span class="ni">🔔</span> Alerts <span id="alertBadge" style="margin-left:auto;background:var(--red);color:#fff;font-size:11px;font-weight:600;padding:1px 7px;border-radius:10px">4</span></div>
    <div class="nav-item"><span class="ni">⚙️</span> Settings</div>
    <div class="sidebar-bottom">
      <div class="nav-item"><span class="ni">👤</span> Admin</div>
    </div>
  </aside>

  <main class="main">
    <header class="topbar">
      <div class="page-title">Laptop Assets</div>
      <div class="topbar-right">
        <div class="search">
          <span style="color:var(--muted);font-size:13px">🔍</span>
          <input type="text" placeholder="Search assets or users..." id="searchInput" oninput="renderTable()">
        </div>
        <button class="btn btn-primary" onclick="openAdd()">+ Add Asset</button>
        <div class="user-btn">AD</div>
      </div>
    </header>

    <div class="content">

      <div class="stats">
        <div class="stat-card">
          <div class="stat-label">Total Laptops</div>
          <div class="stat-row">
            <div class="stat-value" id="s-total">—</div>
            <div class="stat-icon" style="background:#eff6ff">💻</div>
          </div>
          <div class="stat-sub">Registered assets</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">AV Protected</div>
          <div class="stat-row">
            <div class="stat-value" style="color:var(--green)" id="s-prot">—</div>
            <div class="stat-icon" style="background:var(--green-bg)">✅</div>
          </div>
          <div class="stat-sub" id="s-pct">— of fleet</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">No Antivirus</div>
          <div class="stat-row">
            <div class="stat-value" style="color:var(--red)" id="s-unprot">—</div>
            <div class="stat-icon" style="background:var(--red-bg)">⚠️</div>
          </div>
          <div class="stat-sub">Action required</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">AV Expired</div>
          <div class="stat-row">
            <div class="stat-value" style="color:var(--yellow)" id="s-exp">—</div>
            <div class="stat-icon" style="background:var(--yellow-bg)">🔄</div>
          </div>
          <div class="stat-sub">Renewal needed</div>
        </div>
      </div>

      <div class="table-card">
        <div class="table-header">
          <div class="table-title">All Assets</div>
          <div class="table-controls">
            <select id="deptFilter" onchange="renderTable()">
              <option value="">All Departments</option>
              <option>Engineering</option><option>Design</option>
              <option>Marketing</option><option>Finance</option><option>HR</option>
            </select>
            <select id="avFilter" onchange="renderTable()">
              <option value="">All AV Status</option>
              <option value="protected">Protected</option>
              <option value="unprotected">No Antivirus</option>
              <option value="expired">Expired</option>
            </select>
            <select id="stFilter" onchange="renderTable()">
              <option value="">All Status</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
              <option value="maintenance">Maintenance</option>
            </select>
          </div>
        </div>
        <table>
          <thead>
            <tr>
              <th>Asset ID</th><th>Assigned To</th><th>Model</th>
              <th>OS</th><th>Antivirus</th><th>Last Scan</th>
              <th>Status</th><th></th>
            </tr>
          </thead>
          <tbody id="tbody"></tbody>
        </table>
      </div>

      <div class="bottom-row">
        <div class="panel">
          <div class="panel-title">Antivirus Coverage</div>
          <div class="progress-row">
            <div class="progress-label"><span>Protected</span><span id="pb-p">—</span></div>
            <div class="progress-track"><div class="progress-fill" id="pf-p" style="background:var(--green);width:0"></div></div>
          </div>
          <div class="progress-row">
            <div class="progress-label"><span>Expired</span><span id="pb-e">—</span></div>
            <div class="progress-track"><div class="progress-fill" id="pf-e" style="background:var(--yellow);width:0"></div></div>
          </div>
          <div class="progress-row">
            <div class="progress-label"><span>No Antivirus</span><span id="pb-u">—</span></div>
            <div class="progress-track"><div class="progress-fill" id="pf-u" style="background:var(--red);width:0"></div></div>
          </div>
        </div>
        <div class="panel">
          <div class="panel-title">Security Alerts</div>
          <div id="alertList"></div>
        </div>
      </div>

    </div>
  </main>
</div>

<!-- DETAIL -->
<div class="overlay" id="detailOv" onclick="if(event.target===this)closeDetail()">
  <div class="modal">
    <div class="modal-head">
      <h2 id="m-title">—</h2>
      <button class="close-btn" onclick="closeDetail()">✕</button>
    </div>
    <div id="m-banner" class="av-banner"></div>
    <div class="hr"></div>
    <div class="detail-grid" id="m-grid"></div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeDetail()">Close</button>
      <button class="btn btn-primary">Edit Asset</button>
    </div>
  </div>
</div>

<!-- ADD -->
<div class="overlay" id="addOv" onclick="if(event.target===this)closeAdd()">
  <div class="modal">
    <div class="modal-head">
      <h2>Add New Asset</h2>
      <button class="close-btn" onclick="closeAdd()">✕</button>
    </div>
    <div class="form-group"><label class="form-label">Asset ID</label><input class="form-input" id="f-id" placeholder="e.g. LPT-013"></div>
    <div class="form-group"><label class="form-label">Assigned To</label><input class="form-input" id="f-user" placeholder="Full name"></div>
    <div class="form-group"><label class="form-label">Department</label>
      <select class="form-input" id="f-dept"><option>Engineering</option><option>Design</option><option>Marketing</option><option>Finance</option><option>HR</option></select>
    </div>
    <div class="form-group"><label class="form-label">Model</label><input class="form-input" id="f-model" placeholder="e.g. Dell XPS 15"></div>
    <div class="form-group"><label class="form-label">Operating System</label>
      <select class="form-input" id="f-os"><option>Windows 11</option><option>Windows 10</option><option>macOS 14</option><option>Ubuntu 22.04</option></select>
    </div>
    <div class="form-group" style="margin-bottom:18px"><label class="form-label">Antivirus Status</label>
      <select class="form-input" id="f-av"><option value="protected">Protected</option><option value="unprotected">No Antivirus</option><option value="expired">Expired</option></select>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeAdd()">Cancel</button>
      <button class="btn btn-primary" onclick="addAsset()">Add Asset</button>
    </div>
  </div>
</div>

<script>
const ACOLORS=[['#dbeafe','#1d4ed8'],['#dcfce7','#15803d'],['#fce7f3','#be185d'],['#fef3c7','#b45309'],['#ede9fe','#6d28d9'],['#ffedd5','#c2410c']];

let assets=[
  {id:'LPT-001',user:'Aanya Sharma',dept:'Engineering',model:'MacBook Pro 14"',os:'macOS 14',av:'protected',avName:'Malwarebytes',avVer:'4.6.12',lastScan:'2025-03-05',status:'active',since:'Jan 2023'},
  {id:'LPT-002',user:'Rohan Mehta',dept:'Design',model:'Dell XPS 15',os:'Windows 11',av:'unprotected',avName:'—',avVer:'—',lastScan:'Never',status:'active',since:'Jun 2023'},
  {id:'LPT-003',user:'Priya Nair',dept:'Marketing',model:'Lenovo ThinkPad X1',os:'Windows 11',av:'protected',avName:'Windows Defender',avVer:'1.1.23080',lastScan:'2025-03-04',status:'active',since:'Nov 2022'},
  {id:'LPT-004',user:'Vikram Singh',dept:'Finance',model:'HP EliteBook 840',os:'Windows 10',av:'expired',avName:'Norton 360',avVer:'22.23.1',lastScan:'2025-01-15',status:'active',since:'Mar 2022'},
  {id:'LPT-005',user:'Divya Patel',dept:'HR',model:'MacBook Air M2',os:'macOS 14',av:'protected',avName:'CrowdStrike',avVer:'7.1.0',lastScan:'2025-03-05',status:'active',since:'Jan 2024'},
  {id:'LPT-006',user:'Arjun Kumar',dept:'Engineering',model:'Lenovo ThinkPad T14',os:'Ubuntu 22.04',av:'unprotected',avName:'—',avVer:'—',lastScan:'Never',status:'maintenance',since:'Aug 2023'},
  {id:'LPT-007',user:'Sneha Rao',dept:'Engineering',model:'MacBook Pro 16"',os:'macOS 14',av:'protected',avName:'CrowdStrike',avVer:'7.1.0',lastScan:'2025-03-05',status:'active',since:'Mar 2023'},
  {id:'LPT-008',user:'Rahul Gupta',dept:'Marketing',model:'ASUS ZenBook 14',os:'Windows 11',av:'protected',avName:'Bitdefender',avVer:'27.0.20',lastScan:'2025-03-03',status:'active',since:'Feb 2024'},
  {id:'LPT-009',user:'Meera Joshi',dept:'Design',model:'MacBook Air M1',os:'macOS 13',av:'protected',avName:'Malwarebytes',avVer:'4.6.12',lastScan:'2025-03-02',status:'active',since:'Sep 2022'},
  {id:'LPT-010',user:'Karan Bose',dept:'Finance',model:'Dell Latitude 5540',os:'Windows 11',av:'unprotected',avName:'—',avVer:'—',lastScan:'Never',status:'inactive',since:'May 2023'},
  {id:'LPT-011',user:'Anita Desai',dept:'HR',model:'HP ProBook 450',os:'Windows 10',av:'protected',avName:'McAfee',avVer:'16.0.49',lastScan:'2025-03-01',status:'active',since:'Jul 2022'},
  {id:'LPT-012',user:'Sanjay Iyer',dept:'Engineering',model:'Dell XPS 13',os:'Windows 11',av:'protected',avName:'Windows Defender',avVer:'1.1.23080',lastScan:'2025-03-05',status:'active',since:'Mar 2024'},
];

function ini(n){return n.split(' ').map(w=>w[0]).join('').slice(0,2).toUpperCase();}
function acolor(n){let h=0;for(let c of n)h=(h*31+c.charCodeAt(0))%ACOLORS.length;return ACOLORS[Math.abs(h)];}

function avBadge(av){
  if(av==='protected') return `<span class="badge badge-green"><span class="dot" style="background:var(--green)"></span>Protected</span>`;
  if(av==='expired')   return `<span class="badge badge-yellow"><span class="dot" style="background:var(--yellow)"></span>Expired</span>`;
  return `<span class="badge badge-red"><span class="dot" style="background:var(--red)"></span>No Antivirus</span>`;
}

function stBadge(s){
  if(s==='active')   return `<span class="badge badge-green">Active</span>`;
  if(s==='inactive') return `<span class="badge badge-gray">Inactive</span>`;
  return `<span class="badge badge-yellow">Maintenance</span>`;
}

function updateStats(){
  const t=assets.length, p=assets.filter(a=>a.av==='protected').length,
        e=assets.filter(a=>a.av==='expired').length, u=assets.filter(a=>a.av==='unprotected').length;
  document.getElementById('s-total').textContent=t;
  document.getElementById('s-prot').textContent=p;
  document.getElementById('s-unprot').textContent=u;
  document.getElementById('s-exp').textContent=e;
  document.getElementById('s-pct').textContent=t?Math.round(p/t*100)+'% of fleet':'—';
  document.getElementById('pb-p').textContent=p+' device'+(p!==1?'s':'');
  document.getElementById('pb-e').textContent=e+' device'+(e!==1?'s':'');
  document.getElementById('pb-u').textContent=u+' device'+(u!==1?'s':'');
  document.getElementById('pf-p').style.width=t?(p/t*100)+'%':'0';
  document.getElementById('pf-e').style.width=t?(e/t*100)+'%':'0';
  document.getElementById('pf-u').style.width=t?(u/t*100)+'%':'0';
  document.getElementById('alertBadge').textContent=u+e;
}

function renderAlerts(){
  let html='';
  assets.filter(a=>a.av==='unprotected').forEach(a=>{
    html+=`<div class="alert-item"><div class="alert-dot" style="background:var(--red)"></div><div><div class="alert-title">${a.user} — No Antivirus</div><div class="alert-sub">${a.id} · ${a.dept}</div></div><span class="alert-time">Urgent</span></div>`;
  });
  assets.filter(a=>a.av==='expired').forEach(a=>{
    html+=`<div class="alert-item"><div class="alert-dot" style="background:var(--yellow)"></div><div><div class="alert-title">${a.user} — AV Expired</div><div class="alert-sub">${a.id} · ${a.avName}</div></div><span class="alert-time">Renew</span></div>`;
  });
  if(!html) html=`<div class="alert-item"><div class="alert-dot" style="background:var(--green)"></div><div><div class="alert-title">All devices protected</div></div></div>`;
  document.getElementById('alertList').innerHTML=html;
}

function renderTable(){
  const q=document.getElementById('searchInput').value.toLowerCase();
  const dept=document.getElementById('deptFilter').value;
  const av=document.getElementById('avFilter').value;
  const st=document.getElementById('stFilter').value;

  const rows=assets.filter(a=>
    (!q||[a.id,a.user,a.dept,a.model].join(' ').toLowerCase().includes(q))&&
    (!dept||a.dept===dept)&&(!av||a.av===av)&&(!st||a.status===st)
  );

  const tb=document.getElementById('tbody');
  if(!rows.length){tb.innerHTML=`<tr class="empty"><td colspan="8">No assets found</td></tr>`;return;}

  tb.innerHTML=rows.map(a=>{
    const [bg,fg]=acolor(a.user);
    return `<tr>
      <td><span class="asset-id">${a.id}</span></td>
      <td><div class="user-cell">
        <div class="avatar" style="background:${bg};color:${fg}">${ini(a.user)}</div>
        <div><div class="name">${a.user}</div><div class="dept-txt">${a.dept}</div></div>
      </div></td>
      <td class="text-muted">${a.model}</td>
      <td class="text-muted">${a.os}</td>
      <td>${avBadge(a.av)}</td>
      <td class="text-muted mono">${a.lastScan}</td>
      <td>${stBadge(a.status)}</td>
      <td><button class="view-btn" onclick='openDetail(${JSON.stringify(a)})'>View</button></td>
    </tr>`;
  }).join('');
}

function openDetail(a){
  document.getElementById('m-title').textContent=a.id+' · '+a.model;
  const b=document.getElementById('m-banner');
  if(a.av==='protected'){b.style.cssText='background:var(--green-bg);border:1px solid #bbf7d0;color:var(--green)';b.innerHTML=`✅ ${a.avName} v${a.avVer} — Active & up to date`;}
  else if(a.av==='expired'){b.style.cssText='background:var(--yellow-bg);border:1px solid #fde68a;color:var(--yellow)';b.innerHTML=`⚠️ ${a.avName} — License expired`;}
  else{b.style.cssText='background:var(--red-bg);border:1px solid #fecaca;color:var(--red)';b.innerHTML=`🚫 No antivirus installed — device is unprotected`;}
  document.getElementById('m-grid').innerHTML=`
    <div><div class="dl">User</div><div class="dv">${a.user}</div></div>
    <div><div class="dl">Department</div><div class="dv">${a.dept}</div></div>
    <div><div class="dl">Model</div><div class="dv">${a.model}</div></div>
    <div><div class="dl">OS</div><div class="dv">${a.os}</div></div>
    <div><div class="dl">Device Status</div><div class="dv">${a.status.charAt(0).toUpperCase()+a.status.slice(1)}</div></div>
    <div><div class="dl">Assigned Since</div><div class="dv">${a.since}</div></div>
    <div><div class="dl">Last Scan</div><div class="dv">${a.lastScan}</div></div>
    <div><div class="dl">AV Software</div><div class="dv">${a.avName}</div></div>
  `;
  document.getElementById('detailOv').classList.add('open');
}

function closeDetail(){document.getElementById('detailOv').classList.remove('open');}
function openAdd(){document.getElementById('addOv').classList.add('open');}
function closeAdd(){document.getElementById('addOv').classList.remove('open');}

function addAsset(){
  const id=document.getElementById('f-id').value.trim();
  const user=document.getElementById('f-user').value.trim();
  if(!id||!user){alert('Please enter Asset ID and User name.');return;}
  const av=document.getElementById('f-av').value;
  assets.push({id,user,dept:document.getElementById('f-dept').value,model:document.getElementById('f-model').value||'Unknown',os:document.getElementById('f-os').value,av,avName:av==='protected'?'Windows Defender':'—',avVer:av==='protected'?'1.1.23080':'—',lastScan:av==='protected'?new Date().toISOString().slice(0,10):'Never',status:'active',since:new Date().toLocaleDateString('en-US',{month:'short',year:'numeric'})});
  closeAdd();updateStats();renderAlerts();renderTable();
}

updateStats();renderAlerts();renderTable();
</script>
</body>
</html>""")