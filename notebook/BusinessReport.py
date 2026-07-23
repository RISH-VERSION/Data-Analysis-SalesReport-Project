from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

filename = "../reports/business_insights_and_report.pdf"

doc = SimpleDocTemplate(filename, pagesize=letter,
                             topMargin=0.5 * inch, bottomMargin=0.5 * inch,
                             leftMargin=0.5 * inch, rightMargin=0.5 * inch)

styles = getSampleStyleSheet()

story = []
story.append(Paragraph("Business Insights and Reports", styles["Title"]))
story.append(Spacer(1, 12))

story.append(Paragraph("Sales Trend", styles["Heading2"]))
story.append(Image("../screenshots/year+month_full_time_time_superstore.png", width=400, height=300))
story.append(Spacer(1, 12))
story.append(Paragraph("Explanation", styles["Heading3"]))
story.append(Paragraph("This chart shows monthly and yearly sales trends from 2014-2017. Sales demonstrate consistent year-over-year growth, with a repeating seasonal peak every November-December across all four years."))
story.append(Spacer(1, 10))
story.append(Paragraph("Recommendation based on Analysis", styles["Heading3"]))
story.append(Paragraph("Increase inventory stock and staffing ahead of September and November to meet seasonal demand. Introduce targeted promotions in January-February to offset the post-holiday sales slump."))
story.append(Spacer(1, 12))

story.append(Paragraph("Customer Behaviour", styles["Heading2"]))
story.append(Image("../screenshots/Top_sales_per_customer.png", width=400, height=300))
story.append(Image("../screenshots/Top_Profits_Per_customer.png", width=400, height=300))
story.append(Spacer(1, 12))
story.append(Paragraph("Explanation", styles["Heading3"]))
story.append(Paragraph("Tamara Chand leads in profitability (~₹9,000), followed by Raymond Buch and Sanjit Chand. These top profit-generating customers show consistent high-margin purchases rather than volume-driven sales."))
story.append(Spacer(1, 10))
story.append(Paragraph("Recommendation based on Analysis", styles["Heading3"]))
story.append(Paragraph("Focus retention and personalized offers on these top-profit customers since they contribute disproportionately to margins. Analyze their purchase patterns (category/discount level) to replicate this behavior across other high-sales-low-profit customers."))
story.append(Spacer(1, 12))

story.append(Paragraph("Product Performance", styles["Heading2"]))
story.append(Image("../screenshots/Top_10products.png", width=400, height=300))
story.append(Spacer(1, 12))
story.append(Paragraph("Explanation", styles["Heading3"]))
story.append(Paragraph("Canon imageCLASS 2200 Advanced Copier is the top profit-generating product (~₹25,000), nearly 3x the next-best product (Fellowes PB500 binding machine, ~₹7,700). The rest of the top 10 cluster in a similar ₹2,500-4,600 range, showing profit is heavily concentrated in a single flagship product rather than spread evenly."))
story.append(Spacer(1, 10))
story.append(Paragraph("Recommendation based on Analysis", styles["Heading3"]))
story.append(Paragraph("Ensure consistent stock availability and prioritize marketing for the Canon imageCLASS 2200 Advanced Copier given its outsized profit contribution. Investigate what drives its high margin (bundle pricing, low discount) and apply similar strategy to mid-tier products in the same category (copiers/printers) to boost their profitability."))
story.append(Spacer(1, 12))

story.append(Paragraph("Regional Performance", styles["Heading2"]))
story.append(Image("../screenshots/Sales_By_Region_Bar.png", width=400, height=300))
story.append(Image("../screenshots/Sales_By_Region_Pie.png", width=400, height=300))
story.append(Spacer(1, 12))
story.append(Paragraph("Explanation", styles["Heading3"]))
story.append(Paragraph("West (~₹725k) and East (~₹680k) are the top-performing regions by sales, while South (~₹390k) lags significantly behind, roughly 46% lower than West. Central sits in the middle (~₹500k)."))
story.append(Spacer(1, 10))
story.append(Paragraph("Recommendation based on Analysis", styles["Heading3"]))
story.append(Paragraph("Investigate why South underperforms — could be lower store/customer density, weaker marketing presence, or product-mix mismatch. Consider region-specific promotions or expanded distribution to lift South's sales. Study West/East's successful strategies (product mix, discount levels) for replication in weaker regions."))
story.append(Spacer(1, 12))

doc.build(story)
print(f"PDF saved: {filename}")
