from django.shortcuts import render, get_object_or_404, redirect
from conversation.forms import ConversationMessageForm
from conversation.models import Conversation
from core.models import Item


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, item_pk)
    conversations = Conversation.objects.filter(item=item).filter(members__in=request.user.id)

    if item.created_by == request.user:
        return redirect('dashboard:index_page')

    if conversations:
        pass
        # return redirect conversations

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.save()

            return redirect('detail_page', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, '', {
        'conversations': conversations,
        'form': form
    })

