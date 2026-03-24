#!/usr/bin/env python3
"""
SEO Content Engine — Schema/JSON-LD Generator
Generates structured data markup for common page types.
Usage: python generate_schema.py
"""

import json
import sys
from datetime import date


def get_input(prompt, default=None):
    value = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()
    return value if value else default


def generate_article_schema():
    print("\n--- Article Schema ---")
    title = get_input("Article title")
    description = get_input("Meta description (under 160 chars)")
    url = get_input("Full page URL")
    author_name = get_input("Author name")
    org_name = get_input("Publisher / organization name")
    org_logo = get_input("Publisher logo URL")
    date_published = get_input("Date published (YYYY-MM-DD)", str(date.today()))
    date_modified = get_input("Date modified (YYYY-MM-DD)", str(date.today()))
    image_url = get_input("Featured image URL")

    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": url,
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": {
            "@type": "Person",
            "name": author_name
        },
        "publisher": {
            "@type": "Organization",
            "name": org_name,
            "logo": {
                "@type": "ImageObject",
                "url": org_logo
            }
        },
        "image": {
            "@type": "ImageObject",
            "url": image_url
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        }
    }
    return schema


def generate_faq_schema():
    print("\n--- FAQ Schema ---")
    print("Enter FAQ pairs (press Enter with empty question to finish):")
    qa_pairs = []
    i = 1
    while True:
        question = get_input(f"Question {i}")
        if not question:
            break
        answer = get_input(f"Answer {i}")
        qa_pairs.append({"question": question, "answer": answer})
        i += 1

    if not qa_pairs:
        print("No FAQ pairs entered.")
        return None

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": pair["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": pair["answer"]
                }
            }
            for pair in qa_pairs
        ]
    }
    return schema


def generate_howto_schema():
    print("\n--- HowTo Schema ---")
    name = get_input("How-to title (e.g. 'How to Start a Podcast')")
    description = get_input("Brief description")
    total_time = get_input("Total time (ISO 8601, e.g. PT30M for 30 minutes)")
    image_url = get_input("Featured image URL")

    steps = []
    print("Enter steps (press Enter with empty name to finish):")
    i = 1
    while True:
        step_name = get_input(f"Step {i} name")
        if not step_name:
            break
        step_text = get_input(f"Step {i} instructions")
        step_image = get_input(f"Step {i} image URL (optional)")
        step = {
            "@type": "HowToStep",
            "name": step_name,
            "text": step_text
        }
        if step_image:
            step["image"] = step_image
        steps.append(step)
        i += 1

    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "totalTime": total_time,
        "image": image_url,
        "step": steps
    }
    return schema


def generate_local_business_schema():
    print("\n--- Local Business Schema ---")
    business_types = [
        "LocalBusiness", "Restaurant", "MedicalBusiness", "LegalService",
        "FinancialService", "HomeAndConstructionBusiness", "RealEstateAgent",
        "Store", "SportsActivityLocation", "TouristAttraction"
    ]
    print("Business types: " + ", ".join(business_types))
    btype = get_input("Business type", "LocalBusiness")
    name = get_input("Business name")
    description = get_input("Business description")
    url = get_input("Website URL")
    phone = get_input("Phone number (e.g. +1-555-555-5555)")
    street = get_input("Street address")
    city = get_input("City")
    state = get_input("State/Region")
    zip_code = get_input("ZIP/Postal code")
    country = get_input("Country code (e.g. US)", "US")
    lat = get_input("Latitude (optional)")
    lng = get_input("Longitude (optional)")
    price_range = get_input("Price range (e.g. $$)", "$$")

    schema = {
        "@context": "https://schema.org",
        "@type": btype,
        "name": name,
        "description": description,
        "url": url,
        "telephone": phone,
        "priceRange": price_range,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": street,
            "addressLocality": city,
            "addressRegion": state,
            "postalCode": zip_code,
            "addressCountry": country
        }
    }

    if lat and lng:
        schema["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": lat,
            "longitude": lng
        }

    add_hours = get_input("Add opening hours? (y/n)", "n")
    if add_hours.lower() == "y":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        opens = get_input("Opening time (e.g. 09:00)", "09:00")
        closes = get_input("Closing time (e.g. 17:00)", "17:00")
        open_days = get_input("Open days (comma-separated, e.g. Monday,Tuesday)", "Monday,Tuesday,Wednesday,Thursday,Friday")
        day_list = [d.strip() for d in open_days.split(",")]
        schema["openingHoursSpecification"] = [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": day_list,
                "opens": opens,
                "closes": closes
            }
        ]

    return schema


def generate_breadcrumb_schema():
    print("\n--- BreadcrumbList Schema ---")
    print("Enter breadcrumb items from root to current page (press Enter with empty name to finish):")
    items = []
    i = 1
    while True:
        name = get_input(f"Item {i} name (e.g. 'Home')")
        if not name:
            break
        url = get_input(f"Item {i} URL")
        items.append({"name": name, "url": url})
        i += 1

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "name": item["name"],
                "item": item["url"]
            }
            for idx, item in enumerate(items)
        ]
    }
    return schema


def generate_product_schema():
    print("\n--- Product/Review Schema ---")
    name = get_input("Product name")
    description = get_input("Product description")
    image_url = get_input("Product image URL")
    brand = get_input("Brand name")
    sku = get_input("SKU (optional)")
    price = get_input("Price (e.g. 49.99)")
    currency = get_input("Currency code", "USD")
    availability = get_input("Availability (InStock/OutOfStock/PreOrder)", "InStock")
    rating = get_input("Aggregate rating (1-5, optional)")
    review_count = get_input("Number of reviews (optional)")

    schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": name,
        "description": description,
        "image": image_url,
        "brand": {
            "@type": "Brand",
            "name": brand
        },
        "offers": {
            "@type": "Offer",
            "price": price,
            "priceCurrency": currency,
            "availability": f"https://schema.org/{availability}"
        }
    }

    if sku:
        schema["sku"] = sku

    if rating and review_count:
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": rating,
            "reviewCount": review_count
        }

    return schema


def output_schema(schema, schema_type):
    if not schema:
        return

    json_str = json.dumps(schema, indent=2)
    script_tag = f'<script type="application/ld+json">\n{json_str}\n</script>'

    filename = f"schema_{schema_type}_{date.today()}.json"
    with open(filename, "w") as f:
        f.write(script_tag)

    print(f"\n✅ Schema generated! Saved to: {filename}")
    print("\n--- Copy this into your HTML <head> section ---\n")
    print(script_tag)


def main():
    print("=" * 50)
    print("  SEO Content Engine — Schema Generator")
    print("=" * 50)
    print("\nSelect schema type:")
    print("  1. Article")
    print("  2. FAQ")
    print("  3. HowTo")
    print("  4. Local Business")
    print("  5. Breadcrumb")
    print("  6. Product / Review")
    print("  7. Generate All (for a single page)")

    choice = get_input("\nEnter number", "1")

    schemas = {}

    if choice == "1":
        schemas["article"] = generate_article_schema()
    elif choice == "2":
        schemas["faq"] = generate_faq_schema()
    elif choice == "3":
        schemas["howto"] = generate_howto_schema()
    elif choice == "4":
        schemas["local_business"] = generate_local_business_schema()
    elif choice == "5":
        schemas["breadcrumb"] = generate_breadcrumb_schema()
    elif choice == "6":
        schemas["product"] = generate_product_schema()
    elif choice == "7":
        print("\nGenerating all schemas for a single page...")
        schemas["article"] = generate_article_schema()
        schemas["faq"] = generate_faq_schema()
        schemas["breadcrumb"] = generate_breadcrumb_schema()
    else:
        print("Invalid choice.")
        sys.exit(1)

    for schema_type, schema in schemas.items():
        if schema:
            output_schema(schema, schema_type)

    print("\n✅ Done! Paste the script tag(s) into your page's <head> section.")
    print("Validate at: https://search.google.com/test/rich-results")


if __name__ == "__main__":
    main()
