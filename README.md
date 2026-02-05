# Energy Use of Products

A static website for comparing the energy consumption of various products.

## Deployment

This website is automatically deployed to Cloudflare Pages when changes are pushed to the `main` branch.

**Live URL:** https://energy-use-products.apps.owid.io

The deployment workflow:
- Automatically creates a Cloudflare Pages project named `energy-use-products`
- Deploys all files in the repository root
- Assigns the custom domain `energy-use-products.apps.owid.io`

**Note:** DNS propagation can take several hours after the first deployment.

## Files

- `index.html` - Main energy comparison tool interface
- `products_data.json` - Energy consumption data for products
- `convert_excel_to_json.py` - Script to convert Excel data to JSON format
- `Energy use of products.xlsx` - Source data spreadsheet
- `read_excel.py` - Utility to read Excel files

## Making Changes

1. Edit files locally
2. Commit your changes
3. Push to the `main` branch
4. The site will automatically redeploy via GitHub Actions

You can also trigger a manual deployment from the Actions tab in GitHub.
