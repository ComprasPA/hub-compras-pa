"""Hub de Compras PA: atalhos para os portais do setor de Compras."""
import base64
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(page_title="Hub de Compras PA", page_icon=str(ASSETS / "icone_pa.png"),
                   layout="wide", initial_sidebar_state="collapsed")


def b64(nome: str) -> str:
    return base64.b64encode((ASSETS / nome).read_bytes()).decode()


# Ícones em traço (estilo Lucide), herdam a cor do card via currentColor.
ICONES = {
    "carrinho": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/>'
                '<path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
    "comprador": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/>'
                 '<path d="M2 13h20"/><path d="M12 12v2"/>',
    "panorama": '<path d="M3 3v18h18"/><path d="M7 16v-4"/><path d="M11 16V8"/><path d="M15 16v-6"/><path d="M19 16V5"/>',
    "cotacao": '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/>'
               '<path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h8"/><path d="M12 9v12"/>',
    "banco": '<path d="M3 22h18"/><path d="M6 18v-7"/><path d="M10 18v-7"/><path d="M14 18v-7"/><path d="M18 18v-7"/>'
             '<path d="M12 2 20 7H4z"/>',
    "tributo": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/>'
               '<path d="m9 15 6-6"/><circle cx="9.5" cy="9.5" r=".8"/><circle cx="14.5" cy="14.5" r=".8"/>',
}

PORTAIS = [
    {"nome": "Sistema de Compras", "descricao": "Solicitações, pedidos e consulta geral do setor.",
     "resumo": ["Consulta de solicitações e pedidos do TOTVS", "Filtros por departamento e status",
                "Acompanhamento de aprovação e entrega", "Relatório para download em Excel"],
     "url": "https://sistemadecompraspa.streamlit.app/", "icone": "carrinho", "cor": "#62A03A"},
    {"nome": "Painel do Comprador", "descricao": "Carteira e acompanhamento de cada comprador.",
     "resumo": ["Carteira de solicitações por comprador", "Pendências separadas por status",
                "Prioridades e prazos do dia a dia", "Relatório da carteira em Excel"],
     "url": "https://painel-comprador-pa.streamlit.app/", "icone": "comprador", "cor": "#E9A838"},
    {"nome": "Panorama", "descricao": "Visão executiva das pendências de Compras.",
     "resumo": ["Indicadores gerenciais de Suprimentos", "Volume de solicitações em aberto",
                "Evolução das pendências no tempo", "Leitura rápida para a gestão"],
     "url": "https://pendencias-compras.streamlit.app/", "icone": "panorama", "cor": "#4FB3A5"},
    {"nome": "Mapa de Cotação", "descricao": "Monte e compare cotações de fornecedores.",
     "resumo": ["Upload do mapa de cotação", "Comparativo com o histórico de preços",
                "Espelho do pedido por fornecedor", "Exportação em Excel e PDF"],
     "url": "https://meu-mapa-cotacao.streamlit.app/", "icone": "cotacao", "cor": "#D9734E"},
    {"nome": "Dados Bancários", "descricao": "Ficha de pagamento e cadastro bancário de fornecedores.",
     "resumo": ["Ficha de pagamento por Pedido", "Dados bancários do fornecedor",
                "Cadastro que cresce com o uso", "Menos retrabalho no pagamento"],
     "url": "https://dados-bancarios-fornecedores.streamlit.app/", "icone": "banco", "cor": "#8B7FD6"},
    {"nome": "Regime Tributário", "descricao": "Levantamento do regime tributário dos fornecedores.",
     "resumo": ["Status do levantamento por fornecedor", "Regime informado x sugerido pela consulta",
                "Alerta de divergências e lembretes", "Lista para download em Excel"],
     "url": "https://painel-regime-tributario.streamlit.app/", "icone": "tributo", "cor": "#5B9BD5"},
]

# Artifacts publicados no Claude, em atalhos menores abaixo dos portais.
ARTIFACTS = [
    ("Acompanhamento e indicadores", "#62A03A", [
        ("Taboca · Acompanhamento de compras", "Pedidos da obra Taboca",
         "https://claude.ai/artifact/QGA1W5y3V8YsT3MpKfyR2s?sk=mCackCHqJXzC4ui-uA7ewg#pedidos"),
        ("SCs sem Pedido", "Solicitações ainda sem pedido", "https://claude.ai/artifact/KHXc4thP99uJkpQrq2dUuT"),
        ("Volumetria de Compras", "Volume de pedidos e solicitações", "https://claude.ai/artifact/RN8u7B9UbmqQz3Gv8UmrRY"),
        ("Criticidade das Cotações", "Jan a Set/2026", "https://claude.ai/artifact/LRCjUGnXhStmcsrJFM8VCx"),
        ("Lead Time do Processo de Compras", "Tempo da solicitação à entrega",
         "https://claude.ai/artifact/YDhojrDsGdar9AC7edDBch"),
        ("Análise da base de fornecedores", "Perfil da base cadastrada",
         "https://claude.ai/artifact/MQKWrzX7EW956x99gdptJh"),
    ]),
    ("Cotações, contratos e guias", "#E9A838", [
        ("Estudo para Contrato · Peças STIHL", "Compras 2026", "https://claude.ai/artifact/1jfj2iH6XjZ6iGZZJKh71y"),
        ("Topografia Taboca · Equalização", "Equalização de propostas", "https://claude.ai/artifact/3nnNZVcgH8P8DgV5TUvTok"),
        ("Locação de Pick-Up Hilux", "Comparativo de propostas", "https://claude.ai/artifact/HPEbWwDYErr5ivigicDEVf"),
        ("Desktop i7 12ª geração", "Comparativo de cotações", "https://claude.ai/artifact/JwVwjsYe9szX6oorycBWEh"),
        ("Garfo Paleteiro para Munck", "Comparativo de propostas", "https://claude.ai/artifact/GQxuF8arfJTHrw137AwSdu"),
        ("Gerador de Contratos", "Modelos de contrato", "https://claude.ai/artifact/7jeLL1REPmrtBhqKyZNXQG"),
        ("Guia do app Meu Protheus", "Passo a passo de instalação",
         "https://claude.ai/artifact/TeHAeaDi9R5NLvtEQanEYL"),
    ]),
]

st.markdown("""
<style>
#MainMenu, header[data-testid="stHeader"], footer {visibility: hidden;}
.block-container {padding-top: 2.5rem; max-width: 1240px;}
.stApp {background: radial-gradient(1200px 500px at 15% -10%, rgba(98,160,58,.18), transparent 60%),
                     radial-gradient(900px 450px at 100% 0%, rgba(233,168,56,.12), transparent 60%), #0E1512;}
.hub-topo {display: flex; align-items: center; gap: 22px; flex-wrap: wrap; margin-bottom: 6px;}
.hub-topo img {height: 54px;}
.hub-topo .divisor {width: 1px; height: 46px; background: rgba(255,255,255,.15);}
.hub-titulo {font-size: 1.9rem; font-weight: 800; color: #E6EDE8; line-height: 1.1; margin: 0;}
.hub-sub {color: #93A39A; font-size: .95rem; margin: 4px 0 0;}
.hub-secao {color: #93A39A; font-size: .75rem; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase;
            margin: 38px 0 14px;}
.hub-grade {display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;}
@media (max-width: 980px) {.hub-grade {grid-template-columns: repeat(2, 1fr);}}
@media (max-width: 520px) {.hub-grade {grid-template-columns: 1fr;}}
a.hub-card {display: flex; flex-direction: column; gap: 14px; padding: 28px 24px 24px; border-radius: 16px;
            min-height: clamp(360px, calc((100vh - 270px) / 2), 460px);
            background: linear-gradient(160deg, #18241E, #121A16); border: 1px solid rgba(255,255,255,.07);
            text-decoration: none !important; color: #E6EDE8 !important; position: relative; overflow: hidden;
            transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;}
a.hub-card::before {content: ""; position: absolute; inset: 0 0 auto 0; height: 3px; background: var(--cor);}
a.hub-card:hover {transform: translateY(-4px); border-color: var(--cor);
                  box-shadow: 0 14px 34px -14px var(--cor);}
.hub-icone {width: 58px; height: 58px; border-radius: 14px; display: grid; place-items: center;
            color: var(--cor); background: color-mix(in srgb, var(--cor) 16%, transparent);}
.hub-icone svg {width: 30px; height: 30px;}
.hub-nome {font-size: 1.15rem; font-weight: 700; margin: 0;}
.hub-desc {color: #93A39A; font-size: .88rem; margin: 0; line-height: 1.45;}
.hub-resumo {list-style: none; margin: 8px 0 0; padding: 16px 0 0; border-top: 1px solid rgba(255,255,255,.07);
             display: flex; flex-direction: column; gap: 12px; flex: 1;}
.hub-resumo li {display: flex; gap: 10px; align-items: flex-start; color: #C3CEC7; font-size: .86rem;
                line-height: 1.4; margin: 0; padding: 0;}
.hub-resumo li::before {content: ""; flex: none; width: 7px; height: 7px; margin-top: 6px; border-radius: 50%;
                        background: var(--cor);}
.hub-abrir {font-size: .85rem; font-weight: 700; color: var(--cor); display: flex; align-items: center;
            justify-content: center; gap: 6px; padding: 11px 0; border-radius: 10px;
            border: 1px solid color-mix(in srgb, var(--cor) 45%, transparent);
            background: color-mix(in srgb, var(--cor) 10%, transparent); transition: background .18s ease;}
a.hub-card:hover .hub-abrir {background: color-mix(in srgb, var(--cor) 22%, transparent);}
@media (max-width: 980px) {a.hub-card {min-height: 0;}}
a.hub-card:hover .hub-abrir span {transform: translateX(4px);}
.hub-abrir span {transition: transform .18s ease;}
.hub-subsecao {display: flex; align-items: center; gap: 8px; color: #C3CEC7; font-size: .85rem; font-weight: 700;
               margin: 22px 0 10px;}
.hub-subsecao::before {content: ""; width: 8px; height: 8px; border-radius: 2px; background: var(--cor);}
.hub-mini-grade {display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;}
@media (max-width: 980px) {.hub-mini-grade {grid-template-columns: repeat(2, 1fr);}}
@media (max-width: 520px) {.hub-mini-grade {grid-template-columns: 1fr;}}
a.hub-mini {display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 12px;
            background: #141D18; border: 1px solid rgba(255,255,255,.07); border-left: 3px solid var(--cor);
            text-decoration: none !important; color: #E6EDE8 !important;
            transition: transform .15s ease, border-color .15s ease, background .15s ease;}
a.hub-mini:hover {transform: translateY(-2px); border-color: var(--cor); background: #18241E;}
.hub-mini-icone {flex: none; width: 32px; height: 32px; border-radius: 8px; display: grid; place-items: center;
                 color: var(--cor); background: color-mix(in srgb, var(--cor) 14%, transparent);}
.hub-mini-icone svg {width: 17px; height: 17px;}
.hub-mini-texto {min-width: 0; flex: 1;}
.hub-mini-nome {font-size: .88rem; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;}
.hub-mini-desc {font-size: .76rem; color: #93A39A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;}
.hub-mini-seta {flex: none; color: #5E6E65; font-size: .9rem; transition: transform .15s ease, color .15s ease;}
a.hub-mini:hover .hub-mini-seta {color: var(--cor); transform: translateX(3px);}
@media (max-width: 640px) {
  .hub-topo .divisor {display: none;}
  .hub-titulo {font-size: 1.5rem;}
  .signature-fixed {display: none;}
}
.signature-fixed { position: fixed; bottom: 12px; left: 20px; color: #7a8a8a; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; z-index: 999999; pointer-events: none; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hub-topo">
  <img src="data:image/png;base64,{b64('logo_escuro.png')}" alt="Parente Andrade">
  <div class="divisor"></div>
  <div>
    <div class="hub-titulo">Hub de Compras</div>
    <div class="hub-sub">Todos os portais do setor de Suprimentos em um só lugar.</div>
  </div>
</div>
""", unsafe_allow_html=True)

cards = "".join(
    f'<a class="hub-card" href="{p["url"]}" target="_blank" rel="noopener" style="--cor:{p["cor"]}">'
    f'<div class="hub-icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    f'stroke-linecap="round" stroke-linejoin="round">{ICONES[p["icone"]]}</svg></div>'
    f'<div class="hub-nome">{p["nome"]}</div><div class="hub-desc">{p["descricao"]}</div>'
    f'<ul class="hub-resumo">{"".join(f"<li>{item}</li>" for item in p["resumo"])}</ul>'
    f'<div class="hub-abrir">Abrir portal <span>&rarr;</span></div></a>'
    for p in PORTAIS
)
st.markdown(f'<div class="hub-secao">Portais</div><div class="hub-grade">{cards}</div>', unsafe_allow_html=True)

ICONE_ARTIFACT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
                  'stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/>'
                  '<path d="M9 21V9"/></svg>')
grupos = "".join(
    f'<div class="hub-subsecao" style="--cor:{cor}">{grupo}</div><div class="hub-mini-grade">'
    + "".join(
        f'<a class="hub-mini" href="{url}" target="_blank" rel="noopener" title="{nome}" style="--cor:{cor}">'
        f'<div class="hub-mini-icone">{ICONE_ARTIFACT}</div>'
        f'<div class="hub-mini-texto"><div class="hub-mini-nome">{nome}</div><div class="hub-mini-desc">{desc}</div></div>'
        f'<div class="hub-mini-seta">&rarr;</div></a>'
        for nome, desc, url in itens
    )
    + "</div>"
    for grupo, cor, itens in ARTIFACTS
)
st.markdown(f'<div class="hub-secao">Relatórios e análises</div>{grupos}', unsafe_allow_html=True)

st.markdown('<div class="signature-fixed">Created by SS.</div>', unsafe_allow_html=True)
st.markdown('<style>@media (min-width: 641px) {.assinatura-mobile {display:none;}}</style><p class="assinatura-mobile" style="font-size:11px;font-weight:700;color:#7a8a8a;margin-top:24px">Created by SS.</p>', unsafe_allow_html=True)
