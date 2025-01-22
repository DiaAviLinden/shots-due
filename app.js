let userAge = 0; // default user age
let userId = null; // for account identification

// Account creation
function createAccount() {
    userId = Math.floor(Math.random() * 100000); // Random unique ID
    alert("Account created! Your ID is: " + userId);
}

// Login function
function loginUser() {
    userId = document.getElementById("user-id").value;
    if (userId) {
        alert("Logged in with ID: " + userId);
        loadUserAge(); // Load age from database or cookie
    }
}

// Show user age and vaccine schedule based on CDC recommendations
function showVaccineSchedule() {
    userAge = calculateAge(); // Function to get age from user data (e.g., date of birth)
    document.getElementById("user-age").textContent = userAge;

    let vaccineList = getVaccineRecommendations(userAge);
    alert("Vaccine Schedule: " + vaccineList.join(", "));
}

// Email vaccine reminder with user ID
function emailReminder() {
    let vaccineList = getVaccineRecommendations(userAge);
    let subject = "Your Vaccine Schedule Reminder";
    let body = `Your ID is ${userId}. Your current vaccine schedule: ${vaccineList.join(", ")}.`;
    window.location.href = `mailto:example@example.com?subject=${subject}&body=${body}`;
}

// Calculate age (assuming birthdate input or age input)
function calculateAge() {
    return 25; // Simplified, but should be dynamically calculated based on birthdate.
}

// CDC/NIH vaccination recommendations
function getVaccineRecommendations(age) {
    let vaccines = [];
    // Simplified recommendations based on age
    if (age < 1) {
        vaccines.push("Vitamin K");
        vaccines.push("Hepatitis B");
    } else if (age >= 1 && age < 18) {
        vaccines.push("MMR", "DTaP", "Hep A", "Hep B", "IPV");
    } else if (age >= 18 && age < 65) {
        vaccines.push("Tdap", "HPV", "Flu", "Shingles");
    } else if (age >= 65) {
        vaccines.push("Pneumococcal", "Flu", "Shingles");
    }
    return vaccines;
}
