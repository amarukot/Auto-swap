# Updates and Changes

1. Sellers

- photo doesn't display on Seller list page. `{{ seller.web_site }}` was supposed to be `{{ seller.logo }}`
- Website was hardcoded as "lujack.com" for newly created Sellers. Changed to
  `{{ seller.web_site}}`. This was also linking to URL as an internal link if 'http://' was not in front of the URL, edited code to make sure it checks for a correct URL.

2. Styling -

- css styling not being applied. file was misplaced inside templates folder, moved to main folder under static/css.
- restyled seller detail page. just moved Seller name below image of seller.
