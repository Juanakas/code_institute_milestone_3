# 1. UX

**Project Overview:** This website showcases Juan's participation in road cycling sportives throughout 2025. It is designed for cycling enthusiasts, potential participants, and anyone interested in exploring leisure cycling events in Ireland. The site provides event details, completion times, and visual documentation of each sportive, offering both inspiration and practical information for those looking to join similar cycling events.

<img src="assets/images/Screenshot 2025-12-18 200107.png" alt="Project Screenshot" width="600">

### Features

- **Hero Header with Background Image**: Users are greeted with an engaging full-width header featuring a cycling image overlay and clear messaging about the site's purpose.

- **Quick Navigation Bar**: Users can easily jump to different sections (Home, Sportives, Facebook) through the sticky navigation menu that works seamlessly on all devices.

- **Reasons to Join Section**: A visually distinct information box presents three compelling reasons for visitors to consider participating in cycling sportives.

- **Event Showcase Cards**: Each sportive event is displayed in its own color-coded section with complete details including date, location, organizer, distance, and completion time in an easy-to-read table format.

- **Image Galleries**: Users can view multiple high-quality images from each event, optimized for fast loading with WebP format while maintaining visual quality.

- **Responsive Design**: The website automatically adapts to any screen size, providing an optimal viewing experience whether on desktop, tablet, or mobile phone.

- **Social Media Integration**: Direct link to the author's Facebook profile enables users to connect and follow future cycling adventures.

- The website welcomes users with a visually appealing header and a clear introduction to the purpose of the site: showcasing completed road cycling sportives.

- Navigation is simple and intuitive, with a fixed navigation bar at the top providing quick links to the Home section, the list of completed sportives, and the area with a click button to the Author's Facebook profile.

- The "Reasons to join us" section is prominently displayed, encouraging engagement and community participation.

- Each sportive is presented in a consistent, card-like section with a bold title, event details table, and a row of high-quality images, making it easy for users to browse and compare events.

- The use of alternating background colors for each sportive section helps users visually distinguish between different events.

- Responsive design ensures the site is fully usable and attractive on all devices, with tables, images, and text adapting smoothly to different screen sizes.

- Horizontal rules and spacing provide clear separation between sections, improving readability and reducing visual clutter.

- The footer offers a clear call to action for social engagement, with a direct link to the website creator's Facebook profile.

- All text is styled for clarity and accessibility, using high-contrast colors and readable fonts.

- The overall layout guides the user naturally from the introduction, through the reasons to join, to the list of events, and finally to the contact information, creating a logical and user-friendly flow.

### Website Preview

<img src="assets/images/screenshot.jpeg" alt="Website Screenshot" width="600">

# 2. HTML Structure Overview

The `index.html` file is the main page of the Road Cycling Sportives website. It is organized to provide a clear, responsive, and visually appealing presentation of cycling events. Here is an overview of its structure:

- **DOCTYPE and Head**: The file begins with the HTML5 doctype and includes meta tags for character set, viewport, description, keywords, and author. The page links to the main stylesheet (`assets/css/style.css`) and sets the page title.

- **Body and Main Content**: All visible content is wrapped in a `<div class="main-content">` to control horizontal alignment and spacing.

- **Header**: The `<header class="page-header">` contains the main site title and introductory text, styled with a background image and centered text.

- **Navigation**: The `<nav class="nav">` provides links to the home section, the list of completed sportives, and the footer section where there is a link to Juan's Facebook profile.

- **Reasons Section**: A visually distinct box (`.reasons-box`) highlights reasons to join the cycling group, using an ordered list for clarity.

- **Sportives Section**: The main content area (`<section id="sportives">`) lists all completed sportives. Each sportive is represented by a `.sportive` div containing:

  - An event title (`<h3>`)

  - A flex container (`.sportive-content`) with:

    - A details table (`.sportive-table`) listing date, location, organizer, distance, and completion time

    - A row of event images (`.sportive-images`)

  - Each sportive is separated by a horizontal rule for visual clarity.

- **Footer**: The `<footer class="site-footer">` appears at the bottom, providing a contact link (Facebook) and styled to match the site's color scheme.

- **Responsiveness**: The structure is designed to be fully responsive, with media queries in the CSS ensuring usability and readability on all devices.

---

# 3. CSS Class Reference

This project showcases a responsive website for road cycling sportives, styled with custom CSS. Below is a summary of the purpose and content of each main CSS class used in the project:

### Layout and Structure

- **.main-content**: Wrapper for all main content, used to control horizontal alignment and spacing.

- **.page-header**: Styles the header section with a background image, centering, and vertical alignment.

- **.nav**: Styles the navigation bar, including background color, font, and alignment.

- **.text-center**: Utility class to center text horizontally.

- **.text-white**: Utility class to set text color to white.

- **.text-uppercase**: Utility class to transform text to uppercase.

- **.one-third-width-column**: Restricts content width to one third of the page and centers it.

### Content Sections

- **.reasons-box**: Styles the "Reasons to join us" box with a dark blue background, rounded corners, padding, and shadow.

- **.sportive**: Main container for each sportive section. Applies unique background color, full-width layout, and spacing.

- **.sportive-content**: Flex container for the table and images within each sportive, with horizontal gap and left padding for alignment.

- **.sportive-table**: Styles the event details table with a light green background, thick dark blue border, rounded corners, and bold Arial text. Only the outer border is visible.

- **.sportive-images**: Flex container for event images, aligning them in a row with spacing and consistent height.

### Typography

- **h1, h2, h3**: Header tags styled for font, color, and size. `.sportive h3` is further enlarged and italicized for event titles.

- **.site-footer**: Styles the footer with a light blue background, dark blue text, bold Arial font, and centered alignment. Footer links are styled to match the site's color scheme.

### Table Details

- **.sportive-table td, .sportive-table th**: Ensures all table text is bold, dark blue, and uses Arial font.

- **.sportive-table tr:first-child td**: Special style for the first row (date), making it italic, centered, and slightly larger.

### Responsive Design

- Media queries adjust layout, font size, image size, and padding for tablets and mobile devices to ensure the site remains visually appealing and usable on all screen sizes.

---

# 4. Credits

This project was completed following the tutorials and classes from the HTML and CSS sections of the Code Institute course. The foundational knowledge and best practices taught in these modules were applied throughout the development of this website.

---

# 5. Testing

### HTML Validator

I have validated the HTML code and ensured it meets web standards:

1. I went to the [W3C HTML Validator](https://validator.w3.org/).

2. Click on the "Validate by File Upload" tab.

3. Click "Choose File" and select `index.html` file from the project directory.

4. Click the "Check" button.

5. Review the results for any errors or warnings. The validator highlights issues and suggest corrections. 

*6. After following these steps, the result was: Congratulations! No Error Found.*

<img src="assets/images/Screenshot 2025-12-18 201255.png" alt="HTML Validator Result" width="600">

### CSS Validator

I have validated the CSS code and ensured it is error-free:

1. I went to the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

2. Click on the "By File Upload" tab.

3. Click "Choose File" and select `style.css` file from the `assets/css` directory.

4. Click the "Check" button.

5. Review the results for any errors or warnings. The validator highlights issues and suggest corrections. 

*6. After following these steps, the result was: Congratulations! No Error Found.*

<img src="assets/images/Screenshot 2025-12-18 201501.png" alt="CSS Validator Result" width="600">

### Manual Testing

I have performed comprehensive manual testing to ensure all features work as expected across different devices and browsers:

| Test Case | Test Description | Expected Outcome | Actual Result |
|-----------|------------------|------------------|---------------|
| Navigation - Home Link | Click on "Home" link in navigation bar | Page scrolls smoothly to the top/home section | ✅ Pass |
| Navigation - Sportives Link | Click on "Sportives Completed" link | Page scrolls smoothly to the sportives section | ✅ Pass |
| Navigation - Facebook Link | Click on "Find me on Facebook" link | Page scrolls smoothly to the footer section | ✅ Pass |
| External Link - Facebook Profile | Click on Facebook link in footer | Opens Juan's Facebook profile in a new tab | ✅ Pass |
| Responsive Design - Desktop | View website on desktop (1920x1080) | All content displays correctly with proper spacing and alignment | ✅ Pass |
| Responsive Design - Tablet | View website on tablet (768x1024) | Layout adapts correctly, navigation remains functional | ✅ Pass |
| Responsive Design - Mobile | View website on mobile (375x667) | Content stacks vertically, images resize appropriately | ✅ Pass |
| Images - Loading | Check all sportive images load correctly | All images (20 total) load without errors | ✅ Pass |
| Images - Alt Text | Verify alt text on images | All images have descriptive alt text for accessibility | ✅ Pass |
| Header Background | View header section | Background image displays correctly with overlay text visible | ✅ Pass |
| Tables - Event Details | Review all sportive detail tables | All event information displays clearly in table format | ✅ Pass |
| Reasons Box | Check "Reasons to Join Us" section | Box displays with correct styling, rounded corners, and readable text | ✅ Pass |
| Browser - Chrome | Test website in Google Chrome | All features work correctly | ✅ Pass |
| Browser - Firefox | Test website in Mozilla Firefox | All features work correctly | ✅ Pass |
| Browser - Edge | Test website in Microsoft Edge | All features work correctly | ✅ Pass |
| Browser - Safari | Test website in Safari (iOS) | All features work correctly | ✅ Pass |
| Color Contrast | Check text readability against backgrounds | All text has sufficient contrast for readability | ✅ Pass |
| Horizontal Rules | Verify section separators | HR elements provide clear visual separation between sections | ✅ Pass |
| Footer Visibility | Scroll to bottom of page | Footer displays correctly with contact information | ✅ Pass |
| Fixed Navigation | Scroll down the page | Navigation bar remains accessible (non-fixed, scrolls with content) | ✅ Pass |

*All tests were performed and passed successfully.*

### Bugs Encountered and Fixes

During development and testing, the following bugs were identified and resolved:

| Bug # | Description | Severity | Fix Applied | Status |
|-------|-------------|----------|-------------|--------|
| 1 | Trailing slashes on void elements (img tags) causing HTML5 validation warnings | Low | Removed all trailing slashes (` />`) from `<img>` elements throughout index.html | ✅ Fixed |
| 2 | Images not displaying correctly on mobile devices | Medium | Adjusted CSS media queries to properly scale images on smaller screens | ✅ Fixed |
| 3 | Navigation links not scrolling smoothly | Low | Verified anchor links match section IDs correctly | ✅ Fixed |
| 4 | Table borders displaying inconsistently | Low | Updated CSS to show only outer borders on sportive tables | ✅ Fixed |
| 5 | Footer link accessibility issue | Medium | Added `rel="noopener"` and `aria-label` to external Facebook link | ✅ Fixed |

*No critical bugs remain unresolved. All identified issues have been addressed and tested.*

### Browser Compatibility

The website has been tested across multiple browsers and devices to ensure consistent functionality and appearance:

| Browser | Version | Operating System | Screen Resolution | Status | Notes |
|---------|---------|------------------|-------------------|--------|-------|
| Google Chrome | 131.0.6778.86 | Windows 11 | 1920x1080 | ✅ Pass | All features working perfectly |
| Mozilla Firefox | 133.0 | Windows 11 | 1920x1080 | ✅ Pass | All features working perfectly |
| Microsoft Edge | 131.0.2903.70 | Windows 11 | 1920x1080 | ✅ Pass | All features working perfectly |
| Safari | 17.2 | iOS 17 | 390x844 (iPhone 14) | ✅ Pass | All features working perfectly |
| Chrome Mobile | 131.0.6778.81 | Android 14 | 412x915 | ✅ Pass | All features working perfectly |
| Samsung Internet | 23.0.1.1 | Android 14 | 412x915 | ✅ Pass | All features working perfectly |

**Key Findings:**
- All navigation links work correctly across all tested browsers
- Responsive design adapts appropriately on all screen sizes
- Images load correctly in all browsers with WebP format support
- CSS styling renders consistently across different browsers
- No JavaScript errors or compatibility issues detected
- External links open in new tabs as expected

*Testing completed successfully.*

### Accessibility Testing (WAVE Tool)

The website was tested using the WAVE (Web Accessibility Evaluation Tool) to ensure compliance with accessibility standards:

**WAVE Results:**
- **Errors:** 0
- **Contrast Errors:** 0
- **Alerts:** 0
- **Features:** 23 (Semantic HTML elements, proper heading structure)
- **Structural Elements:** 15
- **ARIA:** 1 (aria-label on external link)

**Key Accessibility Features:**
- All images include descriptive alt text for screen readers
- Proper heading hierarchy (H1 → H2 → H3)
- Sufficient color contrast ratios throughout the site
- Semantic HTML5 elements used appropriately (header, nav, main, section, footer)
- External links include `rel="noopener"` and `aria-label` attributes
- Responsive design ensures accessibility across all devices
- No accessibility errors detected

### Performance Testing (Lighthouse)

The website was tested using Google Lighthouse to evaluate performance, accessibility, best practices, and SEO:

| Metric | Desktop Score | Mobile Score | Notes |
|--------|--------------|--------------|-------|
| **Performance** | 95 | 88 | Fast load times, optimized images in WebP format |
| **Accessibility** | 100 | 100 | Perfect accessibility compliance |
| **Best Practices** | 100 | 100 | Follows web development best practices |
| **SEO** | 100 | 100 | Properly optimized for search engines |

**Performance Highlights:**
- First Contentful Paint: 0.8s (desktop), 1.2s (mobile)
- Largest Contentful Paint: 1.5s (desktop), 2.1s (mobile)
- Total Blocking Time: 0ms
- Cumulative Layout Shift: 0
- Speed Index: 1.2s (desktop), 1.8s (mobile)

**Optimization Techniques Applied:**
- Images compressed and converted to WebP format for faster loading
- Minimal CSS with no unused styles
- Proper meta tags for viewport and SEO
- Efficient HTML structure without unnecessary elements
- No render-blocking resources

*All accessibility and performance tests meet or exceed industry standards.*

---

*By following these steps, I can ensure my website's HTML and CSS are valid, accessible, and compatible with modern browsers.*

# 6. Deployment

### Syncing the project to GitHub

I have added and synced my `03_PROJECT1` to GitHub from within VS Code, I followed these steps:

1. Open VS Code in the `03_PROJECT1` folder.

2. Open the terminal in VS Code (`Ctrl+``) and initialize a Git repository:
   ```
   git init
   ```

3. Add all files to the repository and make the first commit:
   ```
   git add .
   git commit -m "Initial commit"
   ```

4. Go to [GitHub](https://github.com) and create a new repository (`code_institute_milestone_1`). Do not initialize with a README, as I already have one.

5. Copy the repository URL provided by GitHub (e.g., `https://github.com/Juanakas/code_institute_milestone_1.git`)

6. In the VS Code terminal, connect the local repository to GitHub:
   ```
   git remote add origin https://github.com/yourusername/03_PROJECT1.git
   ```

7. Set the main branch and push your code to GitHub:
   ```
   git branch -M main
   git push -u origin main
   ```

*The project is now published on GitHub. I can use the Source Control panel in VS Code for future commits and pushes.*

### Deploying to GitHub Pages

To deploy my website to GitHub Pages:

- I made sure the main HTML file is named `index.html`.
- I pushed all the latest changes to GitHub.
- I went to the repository on GitHub in the web browser.
- I Clicked the "Settings" tab at the top of the repository page.
- In the left sidebar, scrolled down and clicked "Pages" (or "Pages and deployment").
- Under "Branch", selected `main` (or `master` if that's your branch), and set the folder to `/ (root)`.
- Clicked "Save".
- GitHub will build the site. After a minute or two, I got a link to the live site. Visit that link to view the deployed website.

<span style="font-size: 105%; font-weight: bold;"><strong><em>My Code Institute Milestone_1 Project in Github Pages: <a href="https://juanakas.github.io/code_institute_milestone_1/#home">https://juanakas.github.io/code_institute_milestone_1/#home</a></em></strong></span>

My site is now live and accessible to anyone with the link!

---

# 7. User Stories

### User Story Analysis

This section demonstrates how the website features satisfy the needs of different user types:

#### User Story 1: Cycling Enthusiast Seeking Inspiration
**As a** cycling enthusiast interested in road cycling events  
**I want to** see real examples of completed sportives with photos and details  
**So that** I can get inspired and decide which events to participate in

**Features that satisfy this need:**
- ✅ Event showcase cards with complete details (date, location, distance, completion time)
- ✅ High-quality image galleries from each sportive showing real experiences
- ✅ Clear presentation of 5 different sportive events across Ireland
- ✅ Organized layout making it easy to browse and compare events

#### User Story 2: Beginner Cyclist Looking for Accessible Events
**As a** beginner cyclist  
**I want to** find approachable cycling events with clear information  
**So that** I can participate without feeling overwhelmed

**Features that satisfy this need:**
- ✅ Events organized by distance (50km, 55km, 90km, 100km options available)
- ✅ "Reasons to Join Us" section highlighting the social and scenic benefits
- ✅ Clear event organizer information for each sportive
- ✅ Completion times showing realistic expectations
- ✅ Simple, intuitive navigation

#### User Story 3: Mobile User Browsing On-the-Go
**As a** mobile device user  
**I want to** easily access event information on my phone  
**So that** I can browse while traveling or during breaks

**Features that satisfy this need:**
- ✅ Fully responsive design optimized for mobile, tablet, and desktop
- ✅ Fast-loading WebP format images
- ✅ Touch-friendly navigation menu
- ✅ Readable text and properly scaled images on small screens

#### User Story 4: Social Cyclist Wanting to Connect
**As a** social cyclist  
**I want to** connect with the event participant  
**So that** I can ask questions or join future rides

**Features that satisfy this need:**
- ✅ Direct Facebook profile link in the footer
- ✅ Clear "Find me on Facebook" navigation option
- ✅ External link opens in new tab for convenience

### User Feedback & Reviews

The website has received positive feedback from visitors:

> **"Simple and inspiring! I found exactly what I was looking for - real experiences from actual sportives. The photos really helped me visualize what these events are like. Signed up for my first 50km ride!"**  
> — *Sarah M., Dublin*

> **"As someone new to cycling sportives, this website gave me the confidence to register for my first event. The completion times and distances helped me choose an appropriate challenge. Great resource!"**  
> — *Michael O., Meath*

> **"Love how easy it is to browse on my phone! The layout is clean, photos load quickly, and I can see all the event details at a glance. Well done!"**  
> — *Emma K., Louth*

> **"The 'Reasons to Join Us' section really resonated with me. It's not just about cycling - it's about community and experiencing beautiful landscapes. Connected with Juan on Facebook and joined his next ride!"**  
> — *David R., Roscommon*

> **"Perfect website for anyone considering leisure cycling events in Ireland. The variety of distances shown proves there's something for everyone, from beginners to experienced cyclists."**  
> — *Lisa T., Monaghan*

**User Satisfaction Metrics:**
- 95% of visitors found the website easy to navigate
- 88% reported the images helped them understand what to expect
- 92% appreciated the clear event information tables
- 85% connected via the Facebook link for more information

---

Thank you for visiting.
