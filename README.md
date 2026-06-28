# Interactive Salary Predictor — ML Simple Linear Regression Visualizer

A beautiful, highly interactive, and real-time dashboard for exploring and visualizing **Simple Linear Regression** models. Adjust parameters dynamically, edit training datasets inline, and watch the regression line and predictions morph instantly.

This project is structured with unique file names to prevent clashing when placed alongside other projects in the same directory.

---

## 👥 Credits & Contributions

- **Machine Learning Logic & Modeling**: Formulated and designed by [The User]. Sets up the OLS regression goals, parameters, default training data structure, and equations.
- **User Interface & Web Engineering**: Crafted by Antigravity (Google DeepMind AI Assistant). Implements the responsive pastel glassmorphism UI, dual-input synchronization, and real-time Chart.js visualizer.

---

## 📂 Project Structure

- **`salary_predictor.html`**: The UI layout skeleton (uses Chart.js CDN and loads custom scripts).
- **`salary_predictor.css`**: Design tokens, glassmorphism card panels, typography, and hover animations.
- **`salary_predictor.js`**: Client-side simple linear regression engine (OLS calculations for $m, c, R^2$), state binder, and Chart.js controller.
- **`salary_predictor.py`**: The original standalone desktop Python command-line and Matplotlib visualizer script.

---

## 🚀 Features

- **Real-Time ML Regression Engine**: Automatically trains an Ordinary Least Squares (OLS) model from scratch in the browser. Calculates slope ($m$), intercept ($c$), and goodness of fit ($R^2$) on every input or data change.
- **Dual-Binding Year Inputs**: Synchronized range slider and numeric input box for adjusting Years of Experience. Supports auto-expanding maximum bounds.
- **Interactive Chart & Guide Crosshairs**: Renders the training scatter points, regression trendline, and active prediction coordinate with dynamic dashed guide lines.
- **Editable Training Database**: Fully interactive table to add new points, delete existing coordinates, or edit values directly.
- **Pre-Configured Dataset Profiles**:
  1. *Standard Tech Industry*: Default linear dataset representing standard linear progression ($R^2 \approx 0.95$).
  2. *High-Growth Startups (Exponential)*: Shows exponential growth to visualize how linear models fit curves.
  3. *Volatile Consulting (High Noise)*: A highly scattered coordinate profile resulting in a low $R^2 \approx 0.40$ fit.

---

## 💻 Running Locally

You can serve the web interface locally without any build steps or server dependencies:

1. Open a terminal in the project directory.
2. Start a local Python server:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and navigate to:
   [http://localhost:8000/salary_predictor.html](http://localhost:8000/salary_predictor.html)

---

## 🌐 Deploying to GitHub Pages

To host this application online for free:

1. Create a repository on your GitHub account.
2. Push your files to the remote repository.
3. In repository Settings -> **Pages**, set the source to deploy from your `main` branch.
4. Your site will be hosted live at:  
   `https://YOUR_GITHUB_USERNAME.github.io/YOUR_REPO_NAME/salary_predictor.html`
