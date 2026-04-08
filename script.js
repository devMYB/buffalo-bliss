// ============================================
// YOUR BLISS IN 716 - INTERACTIVE FUNCTIONALITY
// ============================================

// ============================================
// GLOBAL RENDERERS
// ============================================

function renderGlobalNav() {
    const navContainer = document.getElementById('globalNav');
    if (!navContainer) return;

    const path = window.location.pathname;
    const isSubpage = path.includes('/pages/');
    const prefix = isSubpage ? '../' : '';

    const navItems = [
        { name: 'Home', url: prefix + 'index.html', active: path.endsWith('/index.html') || path.endsWith('/') },
        { name: 'Digital Edition', url: prefix + 'pages/digital-edition.html', active: path.includes('digital-edition.html') },
        { name: 'Articles', url: prefix + 'pages/article.html', active: path.includes('article.html') },
        { name: 'Attractions', url: prefix + 'pages/attractions.html', active: path.includes('attractions.html') },
        { name: 'Events', url: prefix + 'pages/events.html', active: path.includes('events.html') },
        { name: 'Recipes', url: prefix + 'pages/recipes.html', active: path.includes('recipes.html') },
        { name: 'Restaurants', url: prefix + 'pages/restaurant2.html', active: path.includes('restaurant2.html') }
    ];

    const moreItems = [
        { name: 'Request Advertisement', url: prefix + 'pages/request-advertisement.html', active: path.includes('request-advertisement.html') }
    ];

    const isMoreActive = moreItems.some(item => item.active);

    navContainer.innerHTML = `
        <div class="container header-content">
            <a href="${prefix}index.html" class="logo">Your Bliss in 716</a>
            
            <nav class="nav-main">
                <ul class="nav-list">
                    ${navItems.map(item => `
                        <li>
                            <a href="${item.url}" 
                               class="nav-link ${item.active ? 'active' : ''}" 
                               ${item.external ? 'target="_blank" rel="noopener noreferrer"' : ''}>
                                ${item.name}
                            </a>
                        </li>
                    `).join('')}
                    
                    <!-- More Dropdown -->
                    <li class="nav-item-dropdown">
                        <button class="nav-link dropdown-toggle ${isMoreActive ? 'active' : ''}">
                            More <i class="fas fa-chevron-down ml-1" style="font-size: 0.8em;"></i>
                        </button>
                        <ul class="dropdown-menu">
                            ${moreItems.map(item => `
                                <li>
                                    <a href="${item.url}" class="dropdown-link ${item.active ? 'active' : ''}">
                                        ${item.name}
                                    </a>
                                </li>
                            `).join('')}
                        </ul>
                    </li>
                </ul>
            </nav>

            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span><span></span><span></span>
            </button>
        </div>

        <!-- Mobile Navigation -->
        <nav class="mobile-nav" id="mobileNav">
            <ul class="mobile-nav-list">
                ${navItems.map(item => `
                    <li>
                        <a href="${item.url}" 
                           class="mobile-nav-link ${item.active ? 'active' : ''}"
                           ${item.external ? 'target="_blank" rel="noopener noreferrer"' : ''}>
                            ${item.name}
                        </a>
                    </li>
                `).join('')}
                
                <!-- Expanded More items for mobile -->
                <li style="border-top: 1px solid var(--color-divider); margin-top: var(--space-2); padding-top: var(--space-2);">
                    <span class="mobile-nav-link" style="color: var(--color-text-tertiary); font-size: var(--font-size-xs);">MORE</span>
                </li>
                ${moreItems.map(item => `
                    <li>
                        <a href="${item.url}" class="mobile-nav-link ${item.active ? 'active' : ''}">
                            ${item.name}
                        </a>
                    </li>
                `).join('')}
            </ul>
        </nav>
    `;

    // Re-initialize mobile menu toggle
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileNav = document.getElementById('mobileNav');

    if (mobileMenuToggle && mobileNav) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuToggle.classList.toggle('active');
            mobileNav.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        });
    }

    // Dropdown hover behavior for desktop (CSS handles most of it, but click for mobile-like touch)
    const dropdownToggle = navContainer.querySelector('.dropdown-toggle');
    const dropdownMenu = navContainer.querySelector('.dropdown-menu');
    if (dropdownToggle && dropdownMenu) {
        dropdownToggle.addEventListener('click', (e) => {
            if (window.innerWidth < 1024) {
                dropdownMenu.classList.toggle('active');
            }
        });
    }
}

function renderGlobalFooter() {
    const footerContainer = document.querySelector('footer.footer');
    if (!footerContainer) return;

    const path = window.location.pathname;
    const isSubpage = path.includes('/pages/');
    const prefix = isSubpage ? '../' : '';

    footerContainer.innerHTML = `
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Your Bliss in 716</h4>
                    <p style="color: var(--color-neutral-300); margin-bottom: var(--space-4);">
                        Your guide to wellness, inspiration, and discovering the best of Buffalo, NY.
                    </p>
                    <div class="flex gap-4">
                        <!--
                        <a href="#" class="footer-link" aria-label="Facebook"><i class="fab fa-facebook fa-lg"></i></a>
                        <a href="#" class="footer-link" aria-label="Instagram"><i class="fab fa-instagram fa-lg"></i></a>
                        <a href="#" class="footer-link" aria-label="Twitter"><i class="fab fa-twitter fa-lg"></i></a>
                        <a href="#" class="footer-link" aria-label="YouTube"><i class="fab fa-youtube fa-lg"></i></a>
                        -->
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Magazine</h4>
                    <div class="footer-links">
                        <a href="${prefix}pages/digital-edition.html" class="footer-link">Digital Edition</a>
                        <a href="https://yourbliss.us/category/health" class="footer-link" target="_blank">Health</a>
                        <a href="https://yourbliss.us/category/wealth" class="footer-link" target="_blank">Wealth</a>
                        <a href="https://yourbliss.us/category/spirit" class="footer-link" target="_blank">Spirit</a>
                        <a href="https://yourbliss.us/category/happiness" class="footer-link" target="_blank">Happiness</a>
                        <a href="${prefix}pages/recipes.html" class="footer-link">Recipes</a>
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Buffalo Guide</h4>
                    <div class="footer-links">
                        <a href="${prefix}pages/attractions.html" class="footer-link">Attractions</a>
                        <a href="${prefix}pages/events.html" class="footer-link">Events</a>
                        <a href="${prefix}pages/restaurant2.html" class="footer-link">Restaurants</a>
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Contact</h4>
                    <div class="footer-links">
                        <a href="mailto:submit@yourbliss.us" class="footer-link">
                            <i class="fas fa-envelope"></i> submit@yourbliss.us
                        </a>
                        <a href="tel:716-362-7849" class="footer-link">
                            <i class="fas fa-phone"></i> 716-362-7849
                        </a>
                        <a href="#" class="footer-link">About Us</a>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2026 Your Bliss in 716. All rights reserved. | Bringing wellness and Buffalo together.</p>
            </div>
        </div>
    `;
}

// ============================================
// DYNAMIC CONTENT RENDERING
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;
    const isPageIndex = path.endsWith('index.html') || path === '/' || path.endsWith('/');
    const isPageEvents = path.includes('events.html');
    const isPageAttractions = path.includes('attractions.html');
    const isPageDetails = path.includes('details.html');
    const isPageRestaurant2 = path.includes('restaurant2.html');
    const isPageRecipes = path.includes('recipes.html');
    const isRecipeDetail = path.includes('recipe-detail.html');
    const isPageArticle = path.includes('article.html') && !path.includes('article-detail.html');
    const isArticleDetail = path.includes('article-detail.html');
    const isPageDigitalEdition = path.includes('digital-edition.html');

    // Render Global Components
    renderGlobalNav();
    renderGlobalFooter();

    if (isPageIndex) {
        renderFeaturedArticles();
        loadHomepageRecipes();
        renderExploreBuffalo();
        initExploreBuffaloSlider();
    } else if (isPageEvents) {
        loadEvents();
    } else if (isPageAttractions) {
        loadAttractions();
        initAttractionsSlider();
    } else if (isPageDetails) {
        renderDetailPage();
    }
    else if (isPageRestaurant2) {
        loadRestaurantArticles();
    } else if (isPageRecipes) {
        loadRecipes();
    } else if (isRecipeDetail) {
        loadRecipeDetail();
    } else if (isPageArticle) {
        loadArticles();
    } else if (isArticleDetail) {
        loadArticleDetail();
    } else if (isPageDigitalEdition) {
        loadMagazines();
    }

    // Initialize UI components after rendering
    initializeFilters();
    initializeSearch();
    initializeViewToggle();
    initializeSort();
    handleExternalLinks();
    initializeClickableCards();
    renderNewsletterModal();
    initNewsletterLogic();
    initSidebarNewsletter();
});

// Helper to resolve image paths based on current page location
function resolveImagePath(imgSrc) {
    if (!imgSrc) return '';
    if (imgSrc.startsWith('http') || imgSrc.startsWith('//') || imgSrc.startsWith('data:')) {
        return imgSrc;
    }

    // Remove leading dots or slashes if any for consistency
    const cleanPath = imgSrc.replace(/^(\.\.\/|\.\/|\/)/, '');
    const path = window.location.pathname;
    const isSubpage = path.includes('/pages/');

    return isSubpage ? `../${cleanPath}` : cleanPath;
}

async function renderFeaturedArticles() {
    const container = document.getElementById('featuredArticlesContainer');
    if (!container) return;

    try {
        const response = await fetch("http://localhost:8000/api/articles?featured=true");
        const articles = await response.json();

        if (articles.length === 0) {
            // Fallback to static if API is empty or fails (for development)
            if (typeof siteData !== 'undefined' && siteData.articles) {
                renderStaticFeaturedArticles(siteData.articles);
                return;
            }
        }

        container.innerHTML = articles.map(article => `
            <article class="card clickable-card" data-href="pages/article-detail.html?id=${article.id}" role="link" tabindex="0" aria-label="Read article: ${article.name}">
                <img src="${resolveImagePath(article.image)}" alt="${article.name}" class="card-image">
                <div class="card-content">
                    <div class="flex gap-2 mb-4">
                        ${[article.badge1, article.badge2].filter(Boolean).map(badge => `<span class="badge badge-secondary">${badge}</span>`).join('')}
                    </div>
                    <h3 class="card-title">${article.name}</h3>
                    <p class="card-text">${article.description}</p>
                </div>
                <div class="card-footer">
                    <span style="font-size: var(--font-size-sm); color: var(--color-text-tertiary);">
                        <i class="far fa-clock"></i> ${article.minutes} min read
                    </span>
                    <a href="pages/article-detail.html?id=${article.id}" class="btn btn-sm btn-ghost">Read More</a>
                </div>
            </article>
        `).join('');

        initializeClickableCards();
    } catch (err) {
        console.error("Featured articles failed:", err);
        if (typeof siteData !== 'undefined' && siteData.articles) {
            renderStaticFeaturedArticles(siteData.articles);
        }
    }
}

function renderStaticFeaturedArticles(articles) {
    const container = document.getElementById('featuredArticlesContainer');
    if (!container) return;
    container.innerHTML = articles.map(article => `
        <article class="card clickable-card" data-href="${article.url}" role="link" tabindex="0" aria-label="Read article: ${article.title}">
            <img src="${resolveImagePath(article.image)}" alt="${article.title}" class="card-image">
            <div class="card-content">
                <div class="flex gap-2 mb-4">
                    ${article.badges.map(badge => `<span class="badge ${badge === 'Wealth' ? 'badge-accent' : 'badge-secondary'}">${badge}</span>`).join('')}
                </div>
                <h3 class="card-title">${article.title}</h3>
                <p class="card-text">${article.description}</p>
            </div>
            <div class="card-footer">
                <span style="font-size: var(--font-size-sm); color: var(--color-text-tertiary);">
                    <i class="far fa-clock"></i> ${article.readTime}
                </span>
                <a href="${article.url}" class="btn btn-sm btn-ghost">Read More</a>
            </div>
        </article>
    `).join('');
    initializeClickableCards();
}


let allRecipes = [];
let filteredRecipes = [];

async function loadHomepageRecipes() {
    try {
        const response = await fetch("http://localhost:8000/api/recipes");
        const recipes = await response.json();

        const container = document.getElementById("recipesContainer");
        if (!container) return;

        const featured = recipes.filter(r => r.featured);

        const top3 = featured.length >= 3
            ? featured.slice(0, 3)
            : recipes.slice(0, 3); //fallback

        container.innerHTML = top3.map(r => `
            <div class="card clickable-card" data-href="pages/recipe-detail.html?id=${r.id}">
                <img src="${resolveImagePath(r.image)}" class="card-image">
        
                <div class="card-content">
                    <h3 class="card-title">${r.name}</h3>
                    <p class="card-text">${r.description}</p>

                    <div class="flex gap-2 mt-3">
                        ${[r.badge1, r.badge2].filter(Boolean).map(b => `
                            <span class="badge badge-primary">${b}</span>
                        `).join('')}
                    </div>
                </div>
            </div>
        `).join('');

    } catch (err) {
        console.error("Homepage recipes failed:", err);
    }
}

async function loadRecipes() {
    try {
        const response = await fetch("http://localhost:8000/api/recipes");
        const recipes = await response.json();

        allRecipes = recipes;
        filteredRecipes = recipes;

        renderRecipesPageView(recipes);

        initializeRecipeFilters();

    } catch (error) {
        console.error("Error loading recipes:", error);
    }
}

let currentPage = 1;
const RECIPES_PER_PAGE = 6;

function renderRecipesPageView(recipes) {
    if (!recipes) return;

    // =============================
    // 1. FEATURED (TOP PICKS)
    // =============================
    const topContainer = document.getElementById("topPicksContainer");

    if (topContainer) {
        const featured = recipes.filter(r => r.featured);

        topContainer.innerHTML = featured.map(r => `
            <div class="card recipes-card">
                <img src="${resolveImagePath(r.image)}" class="card-image">

                <div class="card-content">
                    <h3 class="card-title">${r.name}</h3>

                    <div class="flex gap-2 mb-3">
                        ${[r.badge1, r.badge2].filter(Boolean).map(b => `
                            <span class="badge badge-primary">${b}</span>
                        `).join('')}
                    </div>
                </div>
            </div>
        `).join('');

        initSlider('topPicksContainer', 'topPicksPrev', 'topPicksNext')
    }

    // =============================
    // 2. PAGINATED MAIN LIST
    // =============================
    renderRecipesPage(recipes, currentPage);
}

function renderRecipesPage(recipes, page) {
    const container = document.getElementById("recipesPageContainer");
    const pagination = document.getElementById("recipesPagination");

    if (!container) return;

    const start = (page - 1) * RECIPES_PER_PAGE;
    const end = start + RECIPES_PER_PAGE;

    const pageRecipes = recipes.slice(start, end);

    // =============================
    // MAIN LAYOUT
    // =============================
    container.innerHTML = pageRecipes.map(r => `
        <article class="recipe-post" data-category="${r.category || ''}">

            <!-- IMAGE LEFT -->
            <a href="recipe-detail.html?id=${r.id}">
                <img 
                    src="${resolveImagePath(r.image)}" 
                    alt="${r.name}" 
                    class="recipe-post-image"
                />
            </a>

            <!-- CONTENT RIGHT -->
            <div class="recipe-post-content">

                <a href="recipe-detail.html?id=${r.id}" style="text-decoration: none; color: inherit;">
                    <h2 class="recipe-post-title">${r.name}</h2>
                </a>

                <p class="recipe-post-description">
                    ${r.description}
                </p>

                <div class="recipe-post-badges">
                    ${[r.badge1, r.badge2].filter(Boolean).map(b => `
                        <span class="badge badge-primary">${b}</span>
                    `).join('')}
                </div>

                <a href="recipe-detail.html?id=${r.id}" class="continue-reading">
                    View Full Recipe →
                </a>
            </div>

        </article>
    `).join('');

    initializeClickableCards();

    // =============================
    // PAGINATION BUTTONS
    // =============================
    if (pagination) {
        const totalPages = Math.ceil(recipes.length / RECIPES_PER_PAGE);

        pagination.innerHTML = Array.from({ length: totalPages }, (_, i) => `
            <button 
                class="pagination-btn ${i + 1 === page ? 'active' : ''}" 
                onclick="changeRecipePage(${i + 1})"
            >
                ${i + 1}
            </button>
        `).join('');
    }
}

function changeRecipePage(page) {
    currentPage = page;
    renderRecipesPage(filteredRecipes, currentPage);
}

async function loadRecipeDetail() {
    const container = document.getElementById('recipeDetailContainer');
    if (!container) return;

    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    if (!id) {
        container.innerHTML = "<p>Recipe not found.</p>";
        return;
    }

    try {
        const response = await fetch(`http://localhost:8000/api/recipes/${id}`);
        const recipe = await response.json();

        renderRecipeDetail(recipe);

    } catch (error) {
        console.error("Error loading recipe:", error);
        container.innerHTML = "<p>Failed to load recipe.</p>";
    }
}

function renderRecipeDetail(recipe) {
    const container = document.getElementById('recipeDetailContainer');
    if (!container || !recipe) return;

    container.innerHTML = `
        <article class="blog-post">

            <!-- TITLE -->
            <h1 class="blog-post-title mb-6">${recipe.name}</h1>
            <br>

            <!-- IMAGE -->
            <img 
                src="${resolveImagePath(recipe.image)}" 
                alt="${recipe.name}" 
                class="blog-post-image"
            >

            <!-- FULL DESCRIPTION -->
            <div class="blog-post-content">
                ${(recipe.full_description || recipe.description)
            .split(/\n\s*\n/)
            .map(p => `<p>${p}</p>`)
            .join('')}
            </div>

            <!-- BADGES -->
            <div class="flex gap-2 mt-6">
                ${[recipe.badge1, recipe.badge2].filter(Boolean).map(b => `
                    <span class="badge badge-primary">${b}</span>
                `).join('')}
            </div>
            <br>
            <br>

            <div class="mt-8">
                <a href="recipes.html" class="btn btn-primary">
                    <i class="fas fa-arrow-left mr-2"></i> Back to Recipes
                </a>
            </div>

        </article>
    `;
}

async function loadRestaurantArticles() {
    try {
        const response = await fetch(`http://localhost:8000/api/restaurants`);

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const restaurants = await response.json();
        renderRestaurantArticles(restaurants);
        handleExternalLinks();
    } catch (error) {
        console.error('Error loading restaurant articles:', error);

        const container = document.getElementById('restaurant2Container');
        if (container) {
            container.innerHTML = `
                <div class="card card-glass" style="padding: 2rem; text-align: center;">
                    <h3>Unable to load restaurants</h3>
                    <p>Please make sure the backend server is running and restaurant data is available.</p>
                </div>
            `;
        }
    }
}

function renderRestaurantArticles(restaurants) {
    const container = document.getElementById('restaurant2Container');
    if (!container || !restaurants) return;

    container.innerHTML = restaurants.map(r => `
        <article class="blog-post">
            <div class="blog-post-header">
                <h2 class="blog-post-title">${r.name}</h2>
                <div class="blog-post-meta">
                    <span><i class="fas fa-map-marker-alt"></i> ${r.address}</span>
                    <span><i class="far fa-compass"></i> ${r.catchy_phrase}</span>
                </div>
            </div>

            <img 
                src="${resolveImagePath(r.image)}" 
                alt="${r.name}" 
                class="blog-post-image"
            >

            <div class="blog-post-content">
                ${(r.description || '')
            .split(/\n\s*\n/)
            .map(paragraph => `<p>${paragraph}</p>`)
            .join('')}
            </div>

            <div class="blog-post-footer">
                ${r.website_url ? `
                    <a href="${r.website_url}" class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer">
                        Visit Website
                    </a>
                ` : ''}

                <div class="blog-post-tags">
                    ${r.badge1 ? `<span class="badge badge-secondary">${r.badge1}</span>` : ''}
                    ${r.badge2 ? `<span class="badge badge-primary">${r.badge2}</span>` : ''}
                </div>
            </div>
        </article>
    `).join('');
}

async function loadEvents() {
    try {
        const response = await fetch(`http://localhost:8000/api/events`);
        if (!response.ok) throw new Error(`API error: ${response.status}`);
        const events = await response.json();
        renderEvents(events);

        //Process newly rendered links
        handleExternalLinks();

        // Re-initialize filters and search after rendering
        initializeFilters();
        initializeSearch();
        initializeClickableCards();
    } catch (error) {
        console.error('Error loading events:', error);
        // Fallback to static data if API fails
        if (typeof siteData !== 'undefined' && siteData.events) {
            renderEvents(siteData.events);
        }
    }
}

/**
 * Format a month string for the event badge so it breaks cleanly
 * into at most 2 lines, never mid-word.
 * Handles: "May", "March - April", "April-December", "Year Round"
 */
function formatMonthBadge(month) {
    if (!month) return '';
    const trimmed = month.trim();
    // "March - April"  →  "MARCH -<br>APRIL"
    if (trimmed.includes(' - ')) {
        const parts = trimmed.split(' - ');
        return parts[0].toUpperCase() + ' -<br>' + parts.slice(1).join(' - ').toUpperCase();
    }
    // "April-December" or "May-August"  →  "APRIL-<br>DECEMBER"
    if (trimmed.includes('-')) {
        const idx = trimmed.indexOf('-');
        return trimmed.slice(0, idx + 1).toUpperCase() + '<br>' + trimmed.slice(idx + 1).toUpperCase();
    }
    // "Year Round"  →  "YEAR<br>ROUND"
    if (trimmed.includes(' ')) {
        const idx = trimmed.indexOf(' ');
        return trimmed.slice(0, idx).toUpperCase() + '<br>' + trimmed.slice(idx + 1).toUpperCase();
    }
    // Single word like "May"
    return trimmed.toUpperCase();
}

function renderEvents(events) {
    const container = document.getElementById('eventsListContainer');
    const featuredContainer = document.getElementById('featuredEventsContainer');
    if (!events) return;

    if (featuredContainer) {
        const featuredEvents = events.filter(e => e.featured);
        featuredContainer.innerHTML = featuredEvents.map(e => `
            <article class="card card-glass clickable-card" 
                data-href="${e.url || '#'}"
                role="link" 
                tabindex="0" 
                aria-label="View details for ${e.name}">
                <img src="${resolveImagePath(e.image)}" alt="${e.name}" style="width: 100%; height: 250px; object-fit: cover; border-radius: var(--radius-xl) var(--radius-xl) 0 0;">
                <div class="card-content">
                    <div class="flex gap-2 mb-4">
                        ${(typeof e.badges === 'string' ? e.badges.split(', ') : (e.badges || [])).map(badge => `<span class="badge ${badge === 'Music' ? 'badge-accent' : 'badge-primary'}">${badge}</span>`).join('')}
                    </div>
                    <h3 class="card-title">${e.name}</h3>
                    <p class="card-text mb-4">${e.description}</p>
                    <div class="event-time">
                        <i class="far fa-calendar"></i> ${e.month}<br>
                        <i class="far fa-clock"></i> ${e.time}<br>
                        <i class="fas fa-map-marker-alt"></i> ${e.location}
                    </div>
                </div>
                <div class="card-footer">
                    ${e.price ? `<span style="font-size: var(--font-size-lg); font-weight: var(--font-weight-bold); color: var(--color-accent);">${e.price}</span>` : ''}
                    <a href="${e.url || '#'}" class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer">Visit Website</a>
                </div>
            </article>
        `).join('');
    }

    if (container) {
        container.innerHTML = events.map(e => `
            <article class="card event-card clickable-card" data-category="${e.category}" data-href="${e.url || '#'}">
                <div class="event-date" style="${e.color ? `background: ${e.color}` : ''}">
                    <span class="event-month">${formatMonthBadge(e.month)}</span>
                </div>
                <div class="event-details">
                    <div class="flex gap-2 mb-3">
                        ${(typeof e.badges === 'string' ? e.badges.split(', ') : (e.badges || [])).map(badge => `<span class="badge ${badge === 'Fitness' ? 'badge-primary' : badge === 'Art' ? 'badge-accent' : 'badge-secondary'}">${badge}</span>`).join('')}
                    </div>
                    <h3 class="card-title">${e.name}</h3>
                    <p class="card-text">${e.description}</p>
                    <div class="event-time">
                        <i class="far fa-clock"></i> ${e.time} | <i class="fas fa-map-marker-alt"></i> ${e.location}
                    </div>
                </div>
                <div style="display: flex; align-items: center;">
                    <a href="${e.url}" class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">
                        Visit Website
                    </a>
                </div>
            </article>
        `).join('');
    }
}


function renderExploreBuffalo() {
    const container = document.getElementById('exploreBuffaloSlider');
    if (!container || !siteData.exploreBuffalo) return;

    container.innerHTML = siteData.exploreBuffalo.map(item => `
        <article class="card card-glass clickable-card" 
            data-href="${item.link}" 
            role="link" 
            tabindex="0" 
            aria-label="Explore ${item.title}">
            <div class="card-content">
                <div style="font-size: 3rem; margin-bottom: var(--space-4);">${item.icon}</div>
                <h3 class="card-title">${item.title}</h3>
                <p class="card-text mb-6">
                    ${item.description}
                </p>
                <div class="flex gap-2 mb-6">
                    ${item.badges.map(badge => `<span class="badge ${badge.includes('Desi') || badge.includes('Cultural') ? 'badge-accent' : badge.includes('Restaurants') || badge.includes('Museums') ? 'badge-primary' : 'badge-secondary'}">${badge}</span>`).join('')}
                </div>
                <a href="${item.link}" class="btn ${item.btnClass}">
                    ${item.btnText} <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </article>
    `).join('');
}


function renderAttractions(attractions) {
    const featuredContainer = document.getElementById('featuredAttractionsContainer');
    const allContainer = document.getElementById('attractionsListContainer');
    if (!attractions) return;

    if (featuredContainer) {
        const featured = attractions.filter(a => a.featured);
        featuredContainer.innerHTML = featured.map(a => `
            <article class="card card-glass clickable-card" 
                data-href="details.html?type=attractions&id=${a.id}" 
                role="link" 
                tabindex="0" 
                aria-label="View details for ${a.name}">
                <img src="${resolveImagePath(a.image)}" alt="${a.name}" style="width: 100%; height: 300px; object-fit: cover; border-radius: var(--radius-xl) var(--radius-xl) 0 0;">
                <div class="card-content">
                    <div class="flex gap-2 mb-4">
                        ${[a.badge1, a.badge2].filter(Boolean).map(badge => `
                            <span class="badge badge-primary">${badge}</span>
                        `).join('')}
                    </div>
                    <h3 class="card-title">${a.name}</h3>
                    <p class="card-text mb-4">${a.description}</p>
                    <div class="attraction-hours">
                        <i class="far fa-clock"></i> ${a.hours} | <i class="fas fa-ticket-alt"></i> ${a.price}
                    </div>
                    <a href="details.html?type=attractions&id=${a.id}" class="btn btn-primary">More Details</a>
                </div>
            </article>
        `).join('');
    }

    if (allContainer) {
        allContainer.innerHTML = attractions.map(a => `
            <article class="card clickable-card" 
                data-category="${a.category}" 
                data-href="details.html?type=attractions&id=${a.id}" 
                role="link" 
                tabindex="0" 
                aria-label="View details for ${a.name}">
                <img src="${resolveImagePath(a.image)}" alt="${a.name}" class="attraction-image">
                <div class="card-content">
                    <h3 class="card-title">${a.name}</h3>
                    <p class="card-text">${a.description}</p>
                    <div class="attraction-hours">
                        <i class="far fa-clock"></i> ${a.hours}<br>
                        <i class="fas fa-ticket-alt"></i> ${a.price}
                    </div>
                    <div class="flex gap-2 mb-4">
                        ${[a.badge1, a.badge2].filter(Boolean).map(badge => `
                            <span class="badge badge-primary">${badge}</span>
                        `).join('')}
                    </div>
                </div>
                <div class="card-footer">
                    <span><i class="fas fa-map-marker-alt"></i> ${a.address || 'Buffalo'}</span>
                    <a href="details.html?type=attractions&id=${a.id}" class="btn btn-sm btn-ghost">Details</a>
                </div>
            </article>
        `).join('');
    }
}

async function loadAttractions() {
    try {
        const response = await fetch("http://localhost:8000/api/attractions");

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const attractions = await response.json();

        renderAttractions(attractions);
        handleExternalLinks();
        initializeFilters();
        initializeClickableCards();

    } catch (error) {
        console.error("Error loading attractions:", error);

        const container = document.getElementById("attractionsListContainer");
        if (container) {
            container.innerHTML = `
                <div class="card card-glass" style="padding: 2rem; text-align: center;">
                    <h3>Unable to load attractions</h3>
                    <p>Please make sure backend is running.</p>
                </div>
            `;
        }
    }
}


// ============================================
// EXTERNAL LINK HANDLER
async function renderDetailPage() {
    const container = document.getElementById('detailPageContent');
    if (!container) return;

    const urlParams = new URLSearchParams(window.location.search);
    const type = urlParams.get('type');
    const id = urlParams.get('id');

    if (!type || !id) {
        container.innerHTML = '<div class="container py-20 text-center"><h2>Item not found</h2><a href="../index.html" class="btn btn-primary mt-4">Back to Home</a></div>';
        return;
    }

    let item;

    try {
        const response = await fetch(`http://localhost:8000/api/${type}/${id}`);
        if (response.ok) {
            item = await response.json();
        }
    } catch (error) {
        console.error(`Error fetching ${type} details:`, error);
    }

    if (!item && siteData[type]) {
        item = siteData[type].find(i => i.id === id || String(i.id) === String(id));
    }

    if (!item) {
        container.innerHTML = '<div class="container py-20 text-center"><h2>Item not found</h2><a href="../index.html" class="btn btn-primary mt-4">Back to Home</a></div>';
        return;
    }

    // Update Page SEO
    document.title = `${item.name} | Your Bliss Hub`;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', item.description);

    container.innerHTML = `
        <section class="detail-hero">
            <img src="${resolveImagePath(item.image)}" alt="${item.name}" class="detail-hero-img">
            <div class="detail-hero-content">
                <div class="container">
                    <h1>${item.name}</h1>
                    <div class="flex gap-2 justify-center">
                        ${(typeof item.badges === 'string' ? item.badges.split(', ') : (item.badges || [])).map(badge => `<span class="badge badge-accent">${badge}</span>`).join('')}
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="detail-grid">
                    <!-- Left Column: Content -->
                    <div class="detail-article">
                        <div class="mb-8">
                            <h2 class="mb-6">About ${item.name}</h2>
                            ${(item.full_description || item.description).split('\n\n').map(p => `<p>${p}</p>`).join('')}
                        </div>
                        
                        <div class="detail-actions" style="display: flex; flex-direction: column; gap: var(--space-4); margin-top: var(--space-8); align-items: flex-start;">
                            <a href="${item.url}" class="btn btn-primary btn-lg" target="_blank" rel="noopener noreferrer">
                                Visit Website <i class="fas fa-external-link-alt ml-2"></i>
                            </a>
                            <a href="attractions.html" class="btn btn-secondary btn-lg">
                                <i class="fas fa-arrow-left mr-2"></i> Back to Attractions
                            </a>
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->
                    <div class="detail-sidebar">
                        <div class="sidebar-box">
                            <h3 class="sidebar-title"><i class="fas fa-info-circle info-icon"></i> Quick Info</h3>
                            <ul class="info-list">
                                <li class="info-item">
                                    <i class="fas fa-map-marker-alt info-icon"></i>
                                    <div>
                                        <strong>Location</strong><br>
                                        ${item.address || 'Buffalo, NY'}
                                    </div>
                                </li>
                                <li class="info-item">
                                    <i class="far fa-clock info-icon"></i>
                                    <div>
                                        <strong>Hours</strong><br>
                                        ${item.hours || 'Varies'}
                                    </div>
                                </li>
                                <li class="info-item">
                                    <i class="fas fa-ticket-alt info-icon"></i>
                                    <div>
                                        <strong>Price</strong><br>
                                        ${item.price || 'Free Admission'}
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <div class="sidebar-box">
                            <h3 class="sidebar-title"><i class="fas fa-envelope info-icon"></i> Stay Inspired</h3>
                            <p class="mb-4" style="font-size: var(--font-size-sm); color: var(--color-text-secondary);">
                                Subscribe to our newsletter for more Buffalo hidden gems and wellness tips.
                            </p>
                            <form class="newsletter-form" onsubmit="event.preventDefault(); alert('Thanks for subscribing!'); this.reset();">
                                <input type="email" class="form-input" placeholder="Your email address" required>
                                <button type="submit" class="btn btn-secondary w-full">Join the Hub</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    `;
}

// ============================================

function handleExternalLinks() {
    const currentHost = window.location.host;
    const links = document.querySelectorAll('a[href]');

    links.forEach(link => {
        const href = link.getAttribute('href');
        // Check if it's an absolute URL and has a different host
        if (href.startsWith('http') || href.startsWith('//')) {
            try {
                const linkUrl = new URL(href, window.location.href);
                if (linkUrl.host !== currentHost) {
                    link.setAttribute('target', '_blank');
                    link.setAttribute('rel', 'noopener noreferrer');
                }
            } catch (e) {
                // If it's an invalid URL, we just skip it
            }
        }
    });
}

// ============================================
// THEME TOGGLE (DARK MODE)
// ============================================

const themeToggle = document.getElementById('themeToggle');
const themeToggleMobile = document.getElementById('themeToggleMobile');
const html = document.documentElement;

const currentTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', currentTheme);

function toggleTheme() {
    const theme = html.getAttribute('data-theme');
    const newTheme = theme === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
if (themeToggleMobile) themeToggleMobile.addEventListener('click', toggleTheme);

// ============================================
// MOBILE NAVIGATION
// ============================================

const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileNav = document.getElementById('mobileNav');

if (mobileMenuToggle && mobileNav) {
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        mobileNav.classList.toggle('active');
        document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
    });

    const mobileNavLinks = mobileNav.querySelectorAll('.mobile-nav-link');
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenuToggle.classList.remove('active');
            mobileNav.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

// ============================================
// SMOOTH SCROLL
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
            }
        }
    });
});

// ============================================
// NEWSLETTER & MODAL LOGIC
// ============================================

async function handleSubscribe(email, form) {
    try {
        const response = await fetch('http://localhost:8000/api/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });
        const data = await response.json();

        if (data.ok) {
            alert(data.message + '!');
            form.reset();
            if (form.id === 'modalNewsletterForm') {
                closeNewsletterModal();
            }
            localStorage.setItem('hasSubscribed', 'true');
        } else {
            alert('Error: ' + data.message);
        }
    } catch (error) {
        console.error('Subscription error:', error);
        alert('Failed to subscribe. Please try again later.');
    }
}

function closeNewsletterModal() {
    const modal = document.getElementById('newsletterModal');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = '';
        localStorage.setItem('newsletterModalDismissed', 'true');
    }
}

function initNewsletterLogic() {
    const bottomForm = document.getElementById('newsletterForm');
    const modalForm = document.getElementById('modalNewsletterForm');
    const modal = document.getElementById('newsletterModal');
    const closeBtn = document.getElementById('closeModal');

    const setupForm = (form) => {
        if (!form) return;
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = form.querySelector('input[type="email"]').value;
            await handleSubscribe(email, form);
        });
    };

    setupForm(bottomForm);
    setupForm(modalForm);

    if (closeBtn) {
        closeBtn.addEventListener('click', closeNewsletterModal);
    }

    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeNewsletterModal();
        });
    }

    // Modal timer logic
    const shouldShow = !localStorage.getItem('hasSubscribed') && !localStorage.getItem('newsletterModalDismissed');
    if (shouldShow && modal) {
        setTimeout(() => {
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }, 8000); // 8 seconds
    }
}

// ============================================
// SCROLL ANIMATIONS
// ============================================

const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

function initializeAnimations() {
    const animatedElements = document.querySelectorAll('.card, .section > .container > *');
    animatedElements.forEach(el => observer.observe(el));
}

document.addEventListener('DOMContentLoaded', initializeAnimations);

// ============================================
// FILTER FUNCTIONALITY
// ============================================

function initializeFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]');

    if (filterButtons.length === 0) return;

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filterableItems = document.querySelectorAll('[data-category]');
            if (filterableItems.length === 0) return;
            const filterValue = (button.getAttribute('data-filter') || 'all').toLowerCase();
            const filterParts = filterValue === 'all' ? [] : filterValue.split(/[ ,]+/).filter(Boolean);

            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            filterableItems.forEach(item => {
                const itemCategoryStr = (item.getAttribute('data-category') || '').toLowerCase();
                const itemCategories = itemCategoryStr.split(/\s+/).filter(Boolean);

                const isMatch = filterValue === 'all' ||
                    filterParts.some(part => itemCategories.includes(part));

                // Clear any pending timeouts by using direct assignment
                if (isMatch) {
                    item.style.display = ''; // Let CSS determine the display property
                    item.style.opacity = '1';
                    item.style.transform = 'scale(1)';
                } else {
                    item.style.display = 'none';
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.9)';
                }
            });
        });
    });
}

function initializeRecipeFilters() {
    const filters = document.querySelectorAll("#recipeTypeFilters .collection-item");
    const searchInput = document.getElementById('searchInput');

    // Handle Category Clicks
    filters.forEach(item => {
        item.addEventListener("click", () => {
            filters.forEach(i => i.classList.remove("active"));
            item.classList.add("active");

            const filter = item.getAttribute("data-filter");
            if (filter === "all") {
                filteredRecipes = allRecipes;
            } else {
                filteredRecipes = allRecipes.filter(r =>
                    filter.split(/[ ,]+/).some(f => r.category.toLowerCase().includes(f))
                );
            }
            currentPage = 1;
            renderRecipesPage(filteredRecipes, currentPage);
        });
    });

    // Handle Search Bar
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            filteredRecipes = allRecipes.filter(r =>
                r.name.toLowerCase().includes(term) ||
                r.description.toLowerCase().includes(term) ||
                (r.category && r.category.toLowerCase().includes(term))
            );
            currentPage = 1;
            renderRecipesPage(filteredRecipes, currentPage);
        });
    }
}


// ============================================
// SEARCH FUNCTIONALITY
// ============================================

function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchableItems = document.querySelectorAll('[data-searchable]');
    if (!searchInput || searchableItems.length === 0) return;

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        searchableItems.forEach(item => {
            const searchableText = item.getAttribute('data-searchable').toLowerCase();
            item.style.display = searchableText.includes(searchTerm) ? '' : 'none';
        });
    });
}

// ============================================
// VIEW TOGGLE
// ============================================

function initializeViewToggle() {
    const viewToggleButtons = document.querySelectorAll('[data-view]');
    const itemsContainer = document.querySelector('.items-container');
    if (viewToggleButtons.length === 0 || !itemsContainer) return;

    viewToggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const view = button.getAttribute('data-view');
            viewToggleButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            if (view === 'grid') {
                itemsContainer.classList.remove('list-view');
                itemsContainer.classList.add('grid-view');
            } else {
                itemsContainer.classList.remove('grid-view');
                itemsContainer.classList.add('list-view');
            }
        });
    });
}

// ============================================
// SORT FUNCTIONALITY
// ============================================

function initializeSort() {
    const sortSelect = document.getElementById('sortSelect');
    const sortableContainer = document.querySelector('[data-sortable-container]');
    if (!sortSelect || !sortableContainer) return;

    sortSelect.addEventListener('change', (e) => {
        const sortBy = e.target.value;
        const items = Array.from(sortableContainer.children);
        items.sort((a, b) => {
            const aValue = a.getAttribute(`data-${sortBy}`);
            const bValue = b.getAttribute(`data-${sortBy}`);
            if (!isNaN(aValue) && !isNaN(bValue)) {
                return sortBy === 'price' ? parseFloat(aValue) - parseFloat(bValue) : parseFloat(bValue) - parseFloat(aValue);
            }
            return aValue.localeCompare(bValue);
        });
        items.forEach(item => sortableContainer.appendChild(item));
    });
}

// ============================================
// CLICKABLE CARDS 
// ============================================

function initializeClickableCards() {
    const clickableCards = document.querySelectorAll('.clickable-card[data-href]');
    clickableCards.forEach(card => {
        const href = card.getAttribute('data-href');
        if (!href) return;

        const handleClick = (e) => {
            const clickedInteractive = e.target.closest('a, button, input, textarea, select, label');
            if (clickedInteractive) return;

            if (e.metaKey || e.ctrlKey || href.startsWith('http')) {
                window.open(href, '_blank', 'noopener');
            } else {
                window.location.href = href;
            }
        };

        card.removeEventListener('click', handleClick);
        card.addEventListener('click', handleClick);
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                handleClick(e);
            }
        });
    });
}

// ============================================
// HEADER SCROLL EFFECT
// ============================================

const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
    header.style.boxShadow = window.pageYOffset > 10 ? 'var(--shadow-md)' : 'none';
});

// ============================================
// GENERIC SLIDER LOGIC
// ============================================

function initSlider(containerId, prevBtnId, nextBtnId) {
    const container = document.getElementById(containerId);
    const prevBtn = document.getElementById(prevBtnId);
    const nextBtn = document.getElementById(nextBtnId);

    if (!container || !prevBtn || !nextBtn) return;

    const getScrollAmount = () => {
        const firstCard = container.querySelector('.card');
        if (!firstCard) return 350;
        const style = window.getComputedStyle(container);
        const gap = parseInt(style.gap) || 24;
        return firstCard.offsetWidth + gap;
    };

    prevBtn.addEventListener('click', () => {
        container.scrollBy({ left: -getScrollAmount(), behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', () => {
        container.scrollBy({ left: getScrollAmount(), behavior: 'smooth' });
    });

    const updateButtons = () => {
        const atStart = container.scrollLeft <= 10;
        const atEnd = container.scrollLeft + container.offsetWidth >= container.scrollWidth - 10;

        prevBtn.style.opacity = atStart ? '0' : '1';
        prevBtn.style.pointerEvents = atStart ? 'none' : 'auto';
        prevBtn.style.visibility = atStart ? 'hidden' : 'visible';

        nextBtn.style.opacity = atEnd ? '0' : '1';
        nextBtn.style.pointerEvents = atEnd ? 'none' : 'auto';
        nextBtn.style.visibility = atEnd ? 'hidden' : 'visible';
    };

    container.addEventListener('scroll', updateButtons);
    window.addEventListener('resize', updateButtons);

    // Initial check
    setTimeout(updateButtons, 100);
}

function initAttractionsSlider() {
    initSlider('featuredAttractionsContainer', 'sliderPrev', 'sliderNext');
}

function initExploreBuffaloSlider() {
    initSlider('exploreBuffaloSlider', 'explorePrev', 'exploreNext');
}


function renderNewsletterModal() {
    // Prevent duplicate injection
    if (document.getElementById('newsletterModal')) return;

    const modalHTML = `
        <div id="newsletterModal" class="modal">
            <div class="modal-content">
                <button class="modal-close" id="closeModal">&times;</button>
                <div class="card card-glass" style="max-width: 700px; margin: 0 auto;">
                    <div class="card-content text-center">
                        <div style="font-size: 3rem; margin-bottom: var(--space-4);"><i class="fas fa-envelope"></i></div>
                        <h2 class="mb-4">Stay Connected</h2>
                        <p class="card-text mb-6">
                            Subscribe to our newsletter for the latest wellness tips, Buffalo events,
                            and exclusive content delivered to your inbox.
                        </p>
                        <form class="newsletter-form" id="modalNewsletterForm">
                            <div class="flex gap-3" style="flex-wrap: wrap;">
                                <input type="email" class="form-input" placeholder="Enter your email address" required
                                    style="flex: 1; min-width: 250px;">
                                <button type="submit" class="btn btn-primary">
                                    Subscribe <i class="fas fa-paper-plane"></i>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);
}

function initSidebarNewsletter() {
    const form = document.getElementById('sidebarNewsletterForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = form.querySelector('input[type="email"]');
        if (emailInput) {
            handleSubscribe(emailInput.value, form);
        }
    });
}

// ============================================
// ARTICLES LOGIC
// ============================================

let allArticles = [];
let filteredArticles = [];
let currentArticlePage = 1;
const ARTICLES_PER_PAGE = 6;

async function loadArticles() {
    try {
        const response = await fetch("http://localhost:8000/api/articles");
        const articles = await response.json();

        allArticles = articles;
        filteredArticles = articles;

        renderArticlesPageView(articles);
        initializeArticleFilters();

        const urlParams = new URLSearchParams(window.location.search);
        const category = urlParams.get('category');
        if (category) {
            applyArticleFilter(category);
        }
    } catch (error) {
        console.error("Error loading articles:", error);
    }
}

function renderArticlesPageView(articles) {
    if (!articles) return;
    const featuredSlider = document.getElementById("featuredArticlesSliderContainer");
    if (featuredSlider) {
        const featured = articles.filter(a => a.featured);
        featuredSlider.innerHTML = featured.map(a => `
            <div class="card clickable-card" data-href="article-detail.html?id=${a.id}">
                <img src="${resolveImagePath(a.image)}" class="card-image" style="height: 200px; object-fit: cover;">
                <div class="card-content">
                    <h3 class="card-title" style="font-size: var(--font-size-lg);">${a.name}</h3>
                    <span class="badge badge-secondary">${a.category.toUpperCase()}</span>
                </div>
            </div>
        `).join('');
        initSlider('featuredArticlesSliderContainer', 'featuredArticlesPrev', 'featuredArticlesNext');
    }
    renderArticlesPage(articles, currentArticlePage);
}

function renderArticlesPage(articles, page) {
    const container = document.getElementById("articlesPageContainer");
    const pagination = document.getElementById("articlesPagination");
    if (!container) return;
    if (articles.length === 0) {
        container.innerHTML = '<div class="text-center py-20"><p>No articles found in this category.</p></div>';
        if (pagination) pagination.innerHTML = '';
        return;
    }
    const start = (page - 1) * ARTICLES_PER_PAGE;
    const end = start + ARTICLES_PER_PAGE;
    const pageArticles = articles.slice(start, end);

    container.innerHTML = pageArticles.map(a => `
        <article class="article-post">
            <a href="article-detail.html?id=${a.id}">
                <img src="${resolveImagePath(a.image)}" alt="${a.name}" class="article-post-image">
            </a>
            <div class="article-post-content">
                <span class="article-post-category">${a.category}</span>
                <a href="article-detail.html?id=${a.id}" style="text-decoration: none; color: inherit;">
                    <h2 class="article-post-title">${a.name}</h2>
                </a>
                <p class="article-post-description">${a.description}</p>
                ${a.author ? `<div class="article-post-author mb-2" style="font-size: var(--font-size-sm); color: var(--color-text-tertiary); font-style: italic;">By ${a.author}</div>` : ''}
                <div class="flex gap-2 mb-4">
                    ${[a.badge1, a.badge2].filter(Boolean).map(b => `<span class="badge badge-secondary">${b}</span>`).join('')}
                </div>
                <a href="article-detail.html?id=${a.id}" class="continue-reading">Read Full Article →</a>
            </div>
        </article>
    `).join('');
    initializeClickableCards();
    if (pagination) {
        const totalPages = Math.ceil(articles.length / ARTICLES_PER_PAGE);
        pagination.innerHTML = Array.from({ length: totalPages }, (_, i) => `
            <button class="pagination-btn ${i + 1 === page ? 'active' : ''}" onclick="changeArticlePage(${i + 1})">
                ${i + 1}
            </button>
        `).join('');
    }
}

function changeArticlePage(page) {
    currentArticlePage = page;
    renderArticlesPage(filteredArticles, currentArticlePage);
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function initializeArticleFilters() {
    const filterItems = document.querySelectorAll('#articleCategoryFilters .collection-item');
    const searchInput = document.getElementById('articleSearchInput');
    filterItems.forEach(item => {
        item.addEventListener('click', () => {
            filterItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            const filter = item.getAttribute('data-filter');
            applyArticleFilter(filter);
        });
    });
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            filteredArticles = allArticles.filter(a =>
                a.name.toLowerCase().includes(term) ||
                a.description.toLowerCase().includes(term) ||
                a.category.toLowerCase().includes(term)
            );
            currentArticlePage = 1;
            renderArticlesPage(filteredArticles, currentArticlePage);
        });
    }
}

function applyArticleFilter(category) {
    if (category === 'all') {
        filteredArticles = allArticles;
    } else {
        filteredArticles = allArticles.filter(a => a.category.toLowerCase() === category.toLowerCase());
    }
    const filterItems = document.querySelectorAll('#articleCategoryFilters .collection-item');
    filterItems.forEach(i => {
        if (i.getAttribute('data-filter') === category) {
            i.classList.add('active');
        } else {
            i.classList.remove('active');
        }
    });
    currentArticlePage = 1;
    renderArticlesPage(filteredArticles, currentArticlePage);
}

async function loadArticleDetail() {
    const container = document.getElementById('articleDetailContainer');
    if (!container) return;
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    if (!id) {
        container.innerHTML = "<p>Article not found.</p>";
        return;
    }
    try {
        const response = await fetch(`http://localhost:8000/api/articles/${id}`);
        const article = await response.json();
        renderArticleDetail(article);
    } catch (error) {
        console.error("Error loading article:", error);
        container.innerHTML = "<p>Failed to load article details.</p>";
    }
}

function renderArticleDetail(article) {
    const container = document.getElementById('articleDetailContainer');
    const titleHeader = document.getElementById('articleMainTitle');
    const descHeader = document.getElementById('articleMainDescription');
    const badgeHeader = document.getElementById('articleBadge');
    if (!container || !article) return;
    if (titleHeader) titleHeader.textContent = article.name;
    if (descHeader) descHeader.textContent = article.description;
    if (badgeHeader) badgeHeader.textContent = article.category.toUpperCase();
    container.innerHTML = `
        <article class="blog-post">
            <img src="${resolveImagePath(article.image)}" alt="${article.name}" class="blog-post-image">
            <div class="blog-post-content">
                ${article.full_description.includes('<')
            ? article.full_description
            : article.full_description.split(/\n\s*\n/).map(p => `<p>${p}</p>`).join('')}
            </div>
            ${article.author ? `<div class="article-author mb-4" style="color: var(--color-text-tertiary); font-style: italic;">By ${article.author}</div>` : ''}
            <div class="flex gap-2 mt-6">
                ${[article.badge1, article.badge2].filter(Boolean).map(b => `<span class="badge badge-secondary">${b}</span>`).join('')}
            </div>
        </article>
        <a href="article.html" class="btn btn-secondary btn-lg">
            <i class="fas fa-arrow-left mr-2"></i> Back to Articles
        </a>
    `;
}

// ============================================
// DIGITAL EDITION - MAGAZINES
// ============================================

async function loadMagazines() {
    const loadingEl = document.getElementById('magazineLoading');
    const container = document.getElementById('magazineYearsContainer');
    if (!container) return;

    try {
        const response = await fetch('http://localhost:8000/api/magazines');
        if (!response.ok) throw new Error(`API error: ${response.status}`);
        const magazines = await response.json();

        if (loadingEl) loadingEl.style.display = 'none';

        if (!magazines || magazines.length === 0) {
            container.innerHTML = `
                <div class="de-empty">
                    <i class="fas fa-book-open"></i>
                    <h2>Coming Soon</h2>
                    <p>Digital editions will be available here shortly. Check back soon!</p>
                </div>`;
            return;
        }

        // Group magazines by year extracted from date_label (e.g. "March 2026" → 2026)
        const byYear = {};
        magazines.forEach(mag => {
            const yearMatch = (mag.name || '').match(/(\d{4})/);
            const year = yearMatch ? yearMatch[1] : 'Other';
            if (!byYear[year]) byYear[year] = [];
            byYear[year].push(mag);
        });

        // Sort years descending (newest first)
        const sortedYears = Object.keys(byYear).sort((a, b) => b - a);

        container.innerHTML = sortedYears.map(year => `
            <section class="year-section">
                <h2 class="year-heading">Digital Edition ${year}</h2>
                <div class="year-divider"></div>
                <div class="magazine-grid">
                    ${byYear[year].map(mag => renderMagazineCard(mag)).join('')}
                </div>
            </section>
        `).join('');

        initMagazineModal();

    } catch (err) {
        console.error('Error loading magazines:', err);
        if (loadingEl) loadingEl.style.display = 'none';
        if (container) {
            container.innerHTML = `
                <div class="de-empty">
                    <i class="fas fa-triangle-exclamation"></i>
                    <h2>Could not load magazines</h2>
                    <p>Please make sure the backend server is running and try again.</p>
                </div>`;
        }
    }
}

function renderMagazineCard(mag) {
    const imageSrc = resolveImagePath(mag.image);
    const fileSrc = resolveImagePath(mag.file);
    const title = mag.name || 'Issue';
    const safeTitle = title.replace(/'/g, "\\'");

    const coverMarkup = imageSrc
        ? `<img src="${imageSrc}" alt="${title} magazine cover" class="magazine-cover" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
           <div class="magazine-cover-placeholder" style="display:none;"><i class="fas fa-book-open"></i><span>${title}</span></div>`
        : `<div class="magazine-cover-placeholder"><i class="fas fa-book-open"></i><span>${title}</span></div>`;

    return `
        <div class="magazine-card"
             role="button"
             tabindex="0"
             aria-label="Read ${title} magazine"
             onclick="openMagazineModal('${fileSrc}', '${safeTitle}')"
             onkeydown="if(event.key==='Enter'||event.key===' ')openMagazineModal('${fileSrc}','${safeTitle}')"
        >
            <div class="magazine-cover-wrap">
                ${coverMarkup}
                <div class="magazine-overlay">
                    <button class="magazine-read-btn" tabindex="-1" aria-hidden="true">
                        <i class="fas fa-book-reader"></i> Read Now
                    </button>
                </div>
                <span class="magazine-free-badge">FREE</span>
            </div>
            <div class="magazine-card-info">
                <div class="magazine-card-title">${title}</div>
            </div>
        </div>`;
}

function initMagazineModal() {
    const backdrop = document.getElementById('pdfModalBackdrop');
    const closeBtn = document.getElementById('pdfModalClose');
    const frame = document.getElementById('pdfFrame');

    if (!backdrop || !closeBtn || !frame) return;

    // Remove old listeners by cloning
    const newClose = closeBtn.cloneNode(true);
    closeBtn.parentNode.replaceChild(newClose, closeBtn);
    newClose.addEventListener('click', closeMagazineModal);

    backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) closeMagazineModal();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeMagazineModal();
    });
}

function openMagazineModal(fileSrc, title) {
    const backdrop = document.getElementById('pdfModalBackdrop');
    const frame = document.getElementById('pdfFrame');
    const titleEl = document.getElementById('pdfModalTitle');
    const dlBtn = document.getElementById('pdfDownloadBtn');
    const fbBtn = document.getElementById('pdfFallbackBtn');
    const fallback = document.getElementById('pdfFallback');

    if (!backdrop || !frame) return;

    if (titleEl) titleEl.textContent = title;
    if (dlBtn) { dlBtn.href = fileSrc; dlBtn.setAttribute('download', title + '.pdf'); }
    if (fbBtn) fbBtn.href = fileSrc;

    // Reset state
    frame.style.display = 'block';
    if (fallback) fallback.style.display = 'none';
    frame.src = fileSrc;

    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeMagazineModal() {
    const backdrop = document.getElementById('pdfModalBackdrop');
    const frame = document.getElementById('pdfFrame');
    if (backdrop) backdrop.classList.remove('active');
    if (frame) frame.src = '';
    document.body.style.overflow = '';
}
