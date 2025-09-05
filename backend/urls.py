urlpatterns += [
    path('api/chat-assistant/', AIChatAssistantView.as_view(), name='chat-assistant'),
]