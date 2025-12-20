"""RSS feed generation utilities."""

from datetime import datetime
from pathlib import Path
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring


def create_rss_feed(
    releases: list,
    title: str,
    link: str,
    description: str,
) -> str:
    """Convert GitHub releases to RSS feed XML.

    Args:
        releases: List of release dictionaries from GitHub API
        title: Feed title
        link: Feed link URL
        description: Feed description

    Returns:
        RSS feed XML string
    """
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")

    # Channel metadata
    title_elem = SubElement(channel, "title")
    title_elem.text = title

    link_elem = SubElement(channel, "link")
    link_elem.text = link

    desc_elem = SubElement(channel, "description")
    desc_elem.text = description

    language = SubElement(channel, "language")
    language.text = "en-us"

    last_build_date = SubElement(channel, "lastBuildDate")
    last_build_date.text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    # Add each release as an item
    for release in releases:
        item = SubElement(channel, "item")

        item_title = SubElement(item, "title")
        item_title.text = release.get("name") or release.get("tag_name", "Unnamed Release")

        item_link = SubElement(item, "link")
        item_link.text = release.get("html_url", "")

        item_description = SubElement(item, "description")
        body = release.get("body", "")
        item_description.text = body if body else "No description provided."

        item_guid = SubElement(item, "guid", isPermaLink="true")
        item_guid.text = release.get("html_url", "")

        # Parse and format the publication date
        published_at = release.get("published_at")
        if published_at:
            pub_date = SubElement(item, "pubDate")
            dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
            pub_date.text = dt.strftime("%a, %d %b %Y %H:%M:%S GMT")

        # Add author if available
        author_info = release.get("author", {})
        if author_info:
            author = SubElement(item, "author")
            author.text = author_info.get("login", "unknown")

    # Pretty print the XML
    xml_string = tostring(rss, encoding="unicode")
    parsed = minidom.parseString(xml_string)
    return parsed.toprettyxml(indent="  ")


def save_feed(
    name: str,
    rss_content: str,
    output_dir: Path,
) -> Path:
    """Save RSS feed to XML file.

    Args:
        name: Feed name (used for filename)
        rss_content: RSS XML content to save
        output_dir: Output directory

    Returns:
        Path to saved XML file
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    xml_path = output_dir / f"{name}.xml"

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(rss_content)

    return xml_path
