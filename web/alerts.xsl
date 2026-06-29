<?xml version="1.0" encoding="UTF-8"?>
<!-- Renders the alerts RSS feed as a readable page when opened in a browser.
     Feed readers ignore this stylesheet and parse the raw RSS. -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/rss/channel">
    <html lang="en">
    <head>
      <meta charset="utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <title><xsl:value-of select="title"/></title>
      <style>
        body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;background:#081620;
          color:#eaf4f2;max-width:780px;margin:0 auto;padding:30px 20px 70px;line-height:1.55;}
        a{color:#3ff0c0;}
        h1{font-size:21px;margin:0 0 4px;}
        .lead{color:#8fa6b2;font-size:14px;margin:0 0 6px;}
        .nav{font-size:13px;margin:10px 0 18px;}
        .it{border-top:1px solid rgba(255,255,255,.12);padding:13px 0;}
        .t{font-weight:600;font-size:15px;}
        .d{color:#9fb3bf;font-size:13.5px;margin-top:3px;}
        .feednote{color:#6f879a;font-size:12px;margin-top:8px;}
      </style>
    </head>
    <body>
      <h1><xsl:value-of select="title"/></h1>
      <p class="lead"><xsl:value-of select="description"/></p>
      <p class="nav"><a href="./alerts.html">Readable alerts page</a> &#183;
        <a href="./?live">Live map</a> &#183; <a href="./">Showcase</a></p>
      <p class="feednote">This is the RSS feed. Paste this page's URL into a feed reader to
        get new leads automatically. The items below are the most recent alerts.</p>
      <xsl:for-each select="item">
        <div class="it">
          <div class="t"><xsl:value-of select="title"/></div>
          <div class="d"><xsl:value-of select="description"/></div>
        </div>
      </xsl:for-each>
    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
