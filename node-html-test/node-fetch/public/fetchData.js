async function fetchData() {
    try {
        const response = await fetch('/api/posts');
        const data = await response.json();
        const postsContainer = document.getElementById('posts');

        postsContainer.innerHTML = data.map(post => `
            <div>
                <h2>${post.title}</h2>
                <p>${post.body}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

window.onload = fetchData;