document.getElementById("event-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const price = parseFloat(document.getElementById("price").value);

    if (!name || isNaN(price) || price <= 0) {
        alert("Insira um nome válido e um preço positivo.");
        return;
    }

    const response = await fetch("http://localhost:3000/products", { // Endpoint permanece o mesmo
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, price }),
    });

    if (response.ok) {
        alert("Evento salvo com sucesso!");
        fetchEvents();
        document.getElementById("event-form").reset();
    } else {
        alert("Erro ao salvar o evento.");
    }
});

async function fetchEvents() {
    const response = await fetch("http://localhost:3000/products");
    const events = await response.json();

    const eventsList = document.getElementById("events-list");
    const emptyMessage = document.getElementById("empty-message");
    const filterInput = document.getElementById("filter");

    eventsList.innerHTML = "";

    if (events.length === 0) {
        emptyMessage.style.display = "block";
        return;
    }

    emptyMessage.style.display = "none";

    events.forEach((event) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${event.id}</td>
            <td>${event.name}</td>
            <td>${event.price.toFixed(2)}</td>
            <td>
                <button class="delete-btn" onclick="deleteEvent(${event.id})">🗑️ Excluir</button>
            </td>
        `;
        eventsList.appendChild(row);
    });

    // Filtro dinâmico
    filterInput.addEventListener("input", () => {
        const searchTerm = filterInput.value.toLowerCase();
        const rows = Array.from(eventsList.querySelectorAll("tr"));
        rows.forEach((row) => {
            const eventName = row.cells[1].textContent.toLowerCase();
            row.style.display = eventName.includes(searchTerm) ? "" : "none";
        });
    });
}

async function deleteEvent(id) {
    const response = await fetch(`http://localhost:3000/products/${id}`, { method: "DELETE" });

    if (response.ok) {
        alert("Evento excluído com sucesso!");
        fetchEvents();
    } else {
        alert("Erro ao excluir o evento.");
    }
}

fetchEvents();
