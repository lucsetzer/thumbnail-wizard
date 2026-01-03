# layout.py - Thumbnail Wizard Layout
def layout(title: str, content: str) -> str:
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>{title} | Thumbnail Wizard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #8b5cf6;
            --primary-hover: #7c3aed;
            --secondary: #f59e0b;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --turquoise: #0d96c1;
        }}
        
        [role="button"], button, .btn-primary {{
            background: var(--primary);
            border-color: var(--primary);
        }}
        
        a {{ color: var(--primary); }}
        a:hover {{ color: var(--primary-hover); }}
        
        /* Cards */
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 2rem 0;
        }}
        
        @media (min-width: 768px) {{
            .card-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}
        
        .step-card {{
            padding: 1.5rem;
            border: 2px solid #e5e7eb;
            border-radius: 0.75rem;
            text-align: center;
            text-decoration: none;
            color: inherit;
            transition: all 0.2s;
            display: block;
            background: white;
        }}
        
        .step-card:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(139, 92, 246, 0.1);
        }}
        
        .step-card i {{
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }}
        
        /* Steps indicator */
        .steps {{
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin: 2rem 0;
        }}
        
        .step {{
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }}
        
        .step.active {{
            background: var(--primary);
            color: white;
        }}
        
        /* Result boxes */
        .result-box {{
            background: #f8fafc !important;
            border: 2px solid #e5e7eb !important;
            border-left: 4px solid var(--primary) !important;
            border-radius: 0.5rem !important;
            padding: 1.5rem !important;
            margin: 1rem 0 !important;
            white-space: pre-wrap !important;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            text-align: left !important;
            color: #1f2937 !important;
            overflow-x: auto;
        }}
        
        .analysis-box {{
            background: #f0f9ff;
            border: 2px solid var(--turquoise);
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin: 1rem 0;
        }}
        
        .score-badge {{
            font-size: 3rem;
            font-weight: bold;
            color: var(--primary);
            text-align: center;
            margin: 1rem 0;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 10px;
            background: #e5e7eb;
            border-radius: 5px;
            overflow: hidden;
            margin: 1rem 0;
        }}
        
        .progress-fill {{
            height: 100%;
            background: var(--primary);
            border-radius: 5px;
        }}
        
        /* Tab switching (simple no-JS version) */
        .tabs {{
            display: flex;
            border-bottom: 2px solid #e5e7eb;
            margin-bottom: 2rem;
        }}
        
        .tab {{
            flex: 1;
            padding: 1rem;
            text-align: center;
            background: #f3f4f6;
            border: none;
            cursor: pointer;
            text-decoration: none;
            color: #6b7280;
        }}
        
        .tab.active {{
            background: var(--primary);
            color: white;
            font-weight: bold;
        }}
    </style>
</head>
<body style="background: white;">
<nav style="padding: 1rem 0; border-bottom: 1px solid #e5e7eb;">
    <div class="container">
        <a href="/" style="text-decoration: none; font-size: 1.25rem; font-weight: bold; color: var(--primary);">
            <i class="fas fa-magic"></i> Thumbnail Wizard
        </a>
        <span style="float: right;">
            <a href="/" style="margin-right: 1rem;">Home</a>
            <a href="/wizard">Thumbnail Wizard</a>
        </span>
    </div>
</nav>

<main class="container" style="padding: 2rem 0; min-height: 80vh;">
    {content}
</main>

<footer style="text-align: center; padding: 2rem; color: #6b7280; border-top: 1px solid #e5e7eb;">
    <p>Thumbnail Wizard • No JavaScript • Pure Python & HTML</p>
</footer>
</body>
</html>'''
