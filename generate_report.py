#!/usr/bin/env python
"""Generate the 100Hires AI SEO Research PDF summary report."""

from fpdf import FPDF
import os

class ResearchPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 5, "100Hires AI-Powered SEO Research", align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 12, 200, 12)
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 51, 102)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def subsection_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(0, 51, 102)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 33, 33)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 33, 33)
        x = self.get_x()
        self.cell(6, 5, "-", new_x="END")
        self.multi_cell(0, 5, text)
        self.ln(1)

    def bold_bullet(self, bold_part, rest):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 33, 33)
        x = self.get_x()
        self.cell(6, 5, "-", new_x="END")
        x2 = self.get_x()
        self.set_font("Helvetica", "B", 10)
        self.cell(self.get_string_width(bold_part) + 1, 5, bold_part)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5, rest)
        self.ln(1)


pdf = ResearchPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# --- Title Page ---
pdf.add_page()
pdf.ln(40)
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 15, "AI-Powered SEO", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 15, "Content Production", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font("Helvetica", "", 16)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 10, "Research Report", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)
pdf.set_draw_color(0, 51, 102)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(15)
pdf.set_font("Helvetica", "", 12)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 8, "100Hires Portfolio Application", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, "June 2026", align="C", new_x="LMARGIN", new_y="NEXT")

# --- Executive Summary ---
pdf.add_page()
pdf.section_title("Executive Summary")
pdf.body_text(
    "The shift from traditional search to AI-powered discovery is fundamentally changing how "
    "content gets found, cited, and ranked. This report presents findings from a comprehensive "
    "research project analyzing how 10 leading practitioners approach AI-powered SEO content "
    "production in 2026."
)
pdf.body_text(
    "Through the analysis of 30+ video transcripts, 10 LinkedIn profiles, and original research "
    "data from Ahrefs, Surfer SEO, and SE Ranking, five major frameworks for AI-powered SEO "
    "emerged. These findings provide a strategic foundation for brands and agencies adapting "
    "to the AI search landscape."
)

# --- Methodology ---
pdf.section_title("Methodology")
pdf.body_text(
    "Ten practitioners were curated based on active YouTube presence (regular uploads within 30 days), "
    "LinkedIn activity, and demonstrated expertise in AI-driven SEO. For each expert, three video "
    "transcripts were collected and analyzed for recurring themes, frameworks, and tactical "
    "recommendations. LinkedIn profiles were documented for recent post themes and engagement patterns."
)

pdf.subsection_title("Experts Researched")
experts = [
    ("Nathan Gotch", "126K", "AEO/GEO, AI search optimization"),
    ("Ahrefs (Sam Oh)", "670K", "SEO education, AEO data research"),
    ("Neil Patel", "1.58M", "Digital marketing, SEO strategy"),
    ("Eric Siu", "200K", "AI marketing, agent workflows"),
    ("Surfer SEO (Matt Kenyon)", "30.3K", "AI search ranking, LLM optimization"),
    ("Joanna Wiebe", "108K", "Conversion copywriting, AI writing"),
    ("Greg Isenberg", "663K", "AI agents, startup growth"),
    ("Tim the SEO Guru", "10.8K", "Claude SEO, ecommerce traffic"),
    ("SE Ranking", "14.4K", "AI visibility, citation strategy"),
    ("Nico AI Ranking", "38.9K", "AI ranking, multi-platform SEO"),
]
col_w = [50, 25, 100]
pdf.set_font("Helvetica", "B", 9)
pdf.set_fill_color(0, 51, 102)
pdf.set_text_color(255, 255, 255)
pdf.cell(col_w[0], 7, "Expert", border=1, fill=True, align="C")
pdf.cell(col_w[1], 7, "Subs", border=1, fill=True, align="C")
pdf.cell(col_w[2], 7, "Focus Area", border=1, fill=True, align="C")
pdf.ln()
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(33, 33, 33)
for name, subs, focus in experts:
    pdf.cell(col_w[0], 6, name, border=1)
    pdf.cell(col_w[1], 6, subs, border=1, align="C")
    pdf.cell(col_w[2], 6, focus, border=1)
    pdf.ln()
pdf.ln(5)

# --- Key Findings ---
pdf.add_page()
pdf.section_title("Key Findings")

# Finding 1
pdf.subsection_title("1. AEO / GEO / LLMO - The New Optimization Layer")
pdf.body_text(
    "Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) have emerged as "
    "distinct disciplines alongside traditional SEO. Multiple experts (Gotch, Ahrefs, Surfer SEO) "
    "agree that optimizing for AI-generated answers requires fundamentally different tactics than "
    "ranking on Google SERPs."
)
pdf.bold_bullet(
    "Question targeting: ",
    "Instead of keyword research (queries people type), AEO requires question research (queries people ask). AI assistants prefer content that directly answers specific questions."
)
pdf.bold_bullet(
    "Structured content: ",
    "Clear headers, bullet points, definitions, and Q&A sections significantly increase AI citation rates."
)
pdf.bold_bullet(
    "Fan-out optimization: ",
    "AI search engines fan out across multiple query interpretations. Content that covers a topic comprehensively outperforms page-level optimization for individual keywords."
)

# Finding 2
pdf.subsection_title("2. Freshness Drives AI Citations")
pdf.body_text(
    "Ahrefs' proprietary research found that 76% of AI-cited pages were updated or published within "
    "the last 30 days. Across all experts studied, content freshness was cited as the single strongest "
    "predictor of AI citation - more important than domain authority or backlink count in several "
    "studies."
)
pdf.bold_bullet(
    "The 30-day rule: ",
    "Content older than 30 days without updates sees significant drop-off in AI citation rates."
)
pdf.bold_bullet(
    "ChatGPT recency bias: ",
    "Pages updated within 7-14 days are significantly more likely to be cited in ChatGPT browsing mode."
)
pdf.bold_bullet(
    "AI Overviews: ",
    "Google AI Overviews show a similar freshness preference, favoring recently updated content."
)

# Finding 3
pdf.subsection_title("3. Entity Depth Over Keyword Density")
pdf.body_text(
    "AI search engines favor topical depth and entity relationships over keyword matching. Content "
    "that thoroughly covers an entity (person, place, concept) with context and structure outperforms "
    "keyword-optimized surface-level content in AI-generated answers."
)
pdf.bold_bullet(
    "Entity building: ",
    "Strong entity associations (Wikipedia, Knowledge Panel, Crunchbase) increase AI citation probability by up to 3x."
)
pdf.bold_bullet(
    "Topical authority: ",
    "Content organized into topical silos around pillar pages signals authority to both Google and AI search engines."
)
pdf.bold_bullet(
    "The specific advantage: ",
    "Specific, verifiable claims (statistics, case studies, named sources) are rewarded over generic statements."
)

# Finding 4
pdf.add_page()
pdf.subsection_title("4. AI Agents for Automated SEO Workflows")
pdf.body_text(
    "Multiple experts (Greg Isenberg, Eric Siu, Tim the SEO Guru) demonstrate AI agent loops that "
    "automate content production, citation monitoring, and ranking optimization. These systems "
    "reduce manual SEO work while maintaining or improving results."
)
pdf.bold_bullet(
    "Multi-agent architecture: ",
    "Research, writing, optimization, and monitoring should be handled by specialized agents, not a single system."
)
pdf.bold_bullet(
    "Human-in-the-loop: ",
    "AI agents flag content for human review based on confidence thresholds. Content with less than 40% AI generation performed best in SE Ranking's 16-month study."
)
pdf.bold_bullet(
    "Automated monitoring: ",
    "Continuous monitoring of AI citations across ChatGPT, Perplexity, Gemini, and Claude enables rapid response to content gaps."
)

# Finding 5
pdf.subsection_title("5. E-E-A-T Signals in the AI Era")
pdf.body_text(
    "Google's E-E-A-T framework remains critical, but its application has evolved. AI citations "
    "increasingly favor content with clear authorship, cited sources, factual accuracy, and "
    "demonstrated expertise."
)
pdf.bold_bullet(
    "Experience: ",
    "First-hand experience (product reviews, case studies, original research) is the strongest differentiator. AI cannot fabricate genuine experience."
)
pdf.bold_bullet(
    "Expertise: ",
    "Content with named, credentialed authors outperforms anonymous or brand-only content."
)
pdf.bold_bullet(
    "Trustworthiness: ",
    "Accuracy, transparency about methodology and affiliations, and consistent factual correctness are heavily weighted."
)
pdf.bold_bullet(
    "AI detection risk: ",
    "SE Ranking's 16-month experiment showed that content exceeding 70% AI generation underperforms over time and risks future algorithm penalties."
)

# --- Conclusion ---
pdf.add_page()
pdf.section_title("Conclusion")
pdf.body_text(
    "The research validates that AI-powered SEO is not a replacement for traditional SEO but an "
    "evolution of it. The fundamentals - quality content, authority building, technical excellence - "
    "remain essential. What has changed is the execution: content must now be structured for AI "
    "extraction, refreshed on a much shorter cycle, and accompanied by strong entity and E-E-A-T signals."
)
pdf.body_text(
    "Brands that adapt to this new landscape by implementing the five frameworks identified in "
    "this research will be positioned to capture the growing share of search traffic flowing through "
    "AI-powered discovery channels."
)
pdf.ln(10)
pdf.set_font("Helvetica", "I", 9)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 5, "Research conducted June 2026 as part of the 100Hires portfolio application process.", align="C")

# Save
output_path = os.path.join(os.path.dirname(__file__), "100Hires_AI_SEO_Research.pdf")
pdf.output(output_path)
print(f"PDF generated: {output_path}")
print(f"Pages: {pdf.page_no()}")
