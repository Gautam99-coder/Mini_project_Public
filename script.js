// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const messageForm = document.getElementById('message-form');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const newChatBtn = document.getElementById('new-chat-btn');
const chatHistory = document.getElementById('chat-history');

// State variables
let conversations = JSON.parse(localStorage.getItem('conversations')) || [];
let currentConversationId = null;

// API settings (replace with your own API key and endpoint)
const API_KEY = 'your-api-key'; // Replace with your actual API key
const API_URL = 'https://api.openai.com/v1/chat/completions'; // Or use another API provider

// Initialize the app
function init() {
    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = Math.min(userInput.scrollHeight, 200) + 'px';
    });

    // Load conversations from localStorage
    loadConversations();
    
    // Create a new chat on page load if there are no conversations
    if (conversations.length === 0) {
        createNewChat();
    } else {
        loadConversation(conversations[0].id);
    }

    // Event listeners
    messageForm.addEventListener('submit', handleSubmit);
    newChatBtn.addEventListener('click', createNewChat);
    
    // Allow sending message with Enter (but new line with Shift+Enter)
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendBtn.click();
        }
    });
}

// Create a new chat
function createNewChat() {
    // Create a new conversation
    const newConversation = {
        id: Date.now().toString(),
        title: 'New Conversation',
        messages: []
    };
    
    // Add to conversations array
    conversations.unshift(newConversation);
    saveConversations();
    
    // Update UI
    updateConversationsList();
    loadConversation(newConversation.id);
}

// Load existing conversations
function loadConversations() {
    updateConversationsList();
}

// Update the sidebar conversation list
function updateConversationsList() {
    chatHistory.innerHTML = '';
    
    conversations.forEach(conversation => {
        const historyItem = document.createElement('div');
        historyItem.classList.add('chat-history-item');
        historyItem.textContent = conversation.title;
        historyItem.dataset.id = conversation.id;
        
        historyItem.addEventListener('click', () => {
            loadConversation(conversation.id);
        });
        
        chatHistory.appendChild(historyItem);
    });
}

// Load a specific conversation
function loadConversation(conversationId) {
    currentConversationId = conversationId;
    const conversation = conversations.find(c => c.id === conversationId);
    
    // Clear chat messages
    chatMessages.innerHTML = '';
    
    // If there are messages, display them
    if (conversation.messages.length > 0) {
        conversation.messages.forEach(msg => {
            addMessageToUI(msg.role, msg.content);
        });
    } else {
        // Show welcome message if no messages
        chatMessages.innerHTML = `
            <div class="welcome-message">
                <h1>ChatAI</h1>
                <p>Your personal AI assistant</p>
            </div>
        `;
    }
    
    // Highlight the current conversation in the sidebar
    document.querySelectorAll('.chat-history-item').forEach(item => {
        if (item.dataset.id === conversationId) {
            item.style.backgroundColor = '#343541';
        } else {
            item.style.backgroundColor = '';
        }
    });
}

// Handle form submission
async function handleSubmit(e) {
    e.preventDefault();
    
    const message = userInput.value.trim();
    if (!message) return;
    
    // Add user message to UI
    addMessageToUI('user', message);
    
    // Clear input and reset height
    userInput.value = '';
    userInput.style.height = 'auto';
    
    // Get the current conversation
    const conversation = conversations.find(c => c.id === currentConversationId);
    
    // Add message to conversation
    conversation.messages.push({
        role: 'user',
        content: message
    });
    
    // If this is the first message, update the conversation title
    if (conversation.messages.length === 1) {
        // Use the first few words as the title
        const titleWords = message.split(' ').slice(0, 4).join(' ');
        conversation.title = titleWords + (message.split(' ').length > 4 ? '...' : '');
        updateConversationsList();
    }
    
    // Save to localStorage
    saveConversations();
    
    // Show typing indicator
    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'message assistant typing-indicator';
    typingIndicator.innerHTML = `
        <div class="avatar">AI</div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;
    chatMessages.appendChild(typingIndicator);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    try {
        // Call the API to get a response
        const response = await getAIResponse(conversation.messages);
        
        // Remove typing indicator
        chatMessages.removeChild(typingIndicator);
        
        // Add AI response to UI
        addMessageToUI('assistant', response);
        
        // Add to conversation
        conversation.messages.push({
            role: 'assistant',
            content: response
        });
        
        // Save to localStorage
        saveConversations();
    } catch (error) {
        // Remove typing indicator
        chatMessages.removeChild(typingIndicator);
        
        // Show error message
        addMessageToUI('assistant', 'Sorry, I encountered an error. Please try again later.');
        console.error('Error:', error);
    }
}

// Get AI response from API
async function getAIResponse(messages) {
    // For a demo without an actual API key, you can use this mock response
    if (!API_KEY || API_KEY === 'your-api-key') {
        return new Promise(resolve => {
            setTimeout(() => {
                const userMessage = messages[messages.length - 1].content;
                resolve(`This is a demo response to your message: "${userMessage}"\n\nTo get real AI responses, you need to:\n1. Get an API key from OpenAI or another provider\n2. Update the API_KEY and API_URL constants in the JavaScript code.`);
            }, 1500);
        });
    }
    
    // For real implementation:
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: messages.map(msg => ({
                    role: msg.role,
                    content: msg.content
                })),
                temperature: 0.7
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error.message);
        }
        
        return data.choices[0].message.content;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Add message to UI
function addMessageToUI(role, content) {
    // Remove welcome message if present
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        chatMessages.removeChild(welcomeMessage);
    }
    
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);
    
    // Use marked.js to render markdown
    const formattedContent = marked.parse(content);
    
    messageDiv.innerHTML = `
        <div class="avatar">${role === 'user' ? 'You' : 'AI'}</div>
        <div class="message-content">${formattedContent}</div>
    `;
    
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    // Apply syntax highlighting to code blocks
    document.querySelectorAll('pre code').forEach((block) => {
        hljs.highlightElement(block);
    });
}

// Save conversations to localStorage
function saveConversations() {
    localStorage.setItem('conversations', JSON.stringify(conversations));
}

// Initialize the app
init();