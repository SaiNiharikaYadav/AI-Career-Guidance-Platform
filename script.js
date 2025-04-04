async function getRecommendations() {
    const skills = document.getElementById('skills').value;
    const interests = document.getElementById('interests').value;
  
    const response = await fetch("http://localhost:5000/recommend", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ skills, interests })
    });
  
    const data = await response.json();
    const output = document.getElementById("output");
    output.innerHTML = "<h3>Recommended Careers:</h3><ul>" + 
      data.map(item => `<li><strong>${item["Job Title"]}</strong>: ${item["Description"]}</li>`).join("") +
      "</ul>";
  }
  