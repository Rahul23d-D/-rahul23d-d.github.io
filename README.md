# Rahul D - AI & Data Science Portfolio

A professional, modern, and responsive e-portfolio website built with HTML, CSS, and JavaScript. This portfolio showcases education, skills, certifications, and contact information for Rahul D, a B.Tech student in Artificial Intelligence and Data Science at Reva University, Bengaluru.

## 🎨 Design Features

- **Modern Color Theme**: Deep Blue (#1e3a8a) and Gold (#f59e0b) gradient design
- **Responsive Layout**: Fully optimized for desktop, tablet, and mobile devices
- **Smooth Animations**: Fade-in effects and hover transitions for enhanced UX
- **Professional Typography**: Clean and readable fonts with proper hierarchy
- **Interactive Navigation**: Sticky navbar with smooth scrolling
- **Accessibility**: Semantic HTML and ARIA-friendly structure

## 📁 Project Structure

```
rahul-portfolio/
├── index.html          # Main HTML file
├── styles.css          # Stylesheet with color theme
├── script.js           # JavaScript for interactivity
├── profile.jpg         # Profile photograph
└── README.md           # This file
```

## 🚀 Deployment on GitHub Pages

Follow these steps to deploy your portfolio on GitHub Pages:

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in to your account
2. Click the **+** icon in the top-right corner and select **New repository**
3. Name your repository: **`Rahul.github.io`** (Replace "Rahul" with your GitHub username)
   - Example: If your GitHub username is `rahul-d`, name it `rahul-d.github.io`
4. Make sure it's set to **Public**
5. Click **Create repository**

### Step 2: Upload Files to GitHub

#### Option A: Using Git Command Line (Recommended)

1. Open your terminal/command prompt
2. Navigate to your portfolio directory:
   ```bash
   cd /path/to/rahul-portfolio
   ```

3. Initialize Git repository:
   ```bash
   git init
   ```

4. Add all files:
   ```bash
   git add .
   ```

5. Commit your changes:
   ```bash
   git commit -m "Initial portfolio commit"
   ```

6. Add the remote repository (replace YOUR_USERNAME with your GitHub username):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io.git
   ```

7. Push to GitHub:
   ```bash
   git branch -M main
   git push -u origin main
   ```

#### Option B: Using GitHub Web Interface

1. Go to your newly created repository
2. Click **Add file** → **Upload files**
3. Drag and drop all files from the portfolio folder
4. Click **Commit changes**

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Scroll down to **Pages** section
4. Under **Source**, select **main** branch
5. Click **Save**
6. Wait a few minutes for GitHub to build your site
7. Your portfolio will be live at: `https://YOUR_USERNAME.github.io`

## 📋 Sections Included

### 1. **Home/Hero Section**
- Profile photograph with circular border
- Name and title
- Call-to-action button

### 2. **About Me**
- Personal introduction
- Background and interests
- Career aspirations

### 3. **Education**
- B.Tech in AI & Data Science
- University and semester information

### 4. **Technical Skills**
- Python
- C Programming
- C++
- Data Structures & Algorithms (DSA)
- DevOps

### 5. **Certifications & Achievements**
- UniToken Certification
- IBM SkillsBuild Certification
- Wadhwani Foundation Certification
- GeeksforGeeks Certification
- DevOps Certification

### 6. **Contact**
- Email address
- Phone number
- Location
- Social media links (LinkedIn, GitHub, Twitter)

## 🎯 Customization Guide

### Change Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #1e3a8a;      /* Change primary color */
    --secondary-color: #f59e0b;    /* Change accent/gold color */
    --accent-color: #3b82f6;       /* Change bright blue */
    /* ... other colors ... */
}
```

### Update Contact Information

Edit the contact section in `index.html`:

```html
<a href="mailto:your-email@gmail.com">your-email@gmail.com</a>
<a href="tel:+91XXXXXXXXXX">+91 XXXXXXXXXX</a>
```

### Add Social Media Links

Update the social links in the contact section:

```html
<a href="https://linkedin.com/in/yourprofile" class="social-icon">
    <i class="fab fa-linkedin"></i>
</a>
```

### Update Profile Photo

Replace `profile.jpg` with your own image (ensure it's in the same directory)

## 🌐 Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: Below 768px

## ✨ Features

- ✅ Fully responsive design
- ✅ Smooth scroll navigation
- ✅ Hover effects and animations
- ✅ Mobile-friendly hamburger menu
- ✅ Professional color scheme
- ✅ Fast loading performance
- ✅ SEO-friendly structure
- ✅ Easy to customize

## 🔧 Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactivity and smooth scrolling
- **Font Awesome**: Icon library
- **GitHub Pages**: Free hosting

## 📝 Tips for Enhancement

1. **Add Projects Section**: Create a dedicated section for your projects with descriptions and links
2. **Blog Section**: Add a blog to share your learning journey
3. **Dark Mode**: Implement a toggle for dark/light theme
4. **Contact Form**: Add a functional contact form using services like Formspree
5. **Analytics**: Add Google Analytics to track visitors
6. **SEO Optimization**: Add meta tags and structured data

## 🤝 Contributing & Feedback

Feel free to customize this template to match your personal brand and style. Share your portfolio with friends and mentors for feedback!

## 📄 License

This portfolio template is free to use and modify for personal purposes.

## 🎓 About

**Name**: Rahul D  
**Program**: B.Tech in Artificial Intelligence & Data Science  
**University**: Reva University, Bengaluru  
**Semester**: 2nd  
**Email**: rahul@gmail.com  
**Phone**: +91 6364938384

---

**Last Updated**: June 2024

For questions or support, feel free to reach out via email or phone!
