# -*- coding: utf-8 -*-
"""Script to populate a significant load of comments and replies for a specific request ID."""

import os
import random

import requests

# Configuration
BASE_URL = os.getenv("AUTOPOP_BASE_URL")  # Update this to your instance URL
ACCESS_TOKEN = os.getenv(
    "AUTOPOP_ACCESS_TOKEN"
)  # Update this with a valid access token
REQUEST_ID = os.getenv("AUTOPOP_REQUEST_ID")


# Number of items to create
NUM_TOP_LEVEL_COMMENTS = 50  # Number of parent comments
NUM_REPLIES_PER_COMMENT = 3  # Number of replies per parent comment

# Randomized content generators
COMMENT_STARTERS = [
    "I know",
    "I think",
    "In my opinion",
    "Based on my analysis",
    "After reviewing this",
    "Looking at the details",
    "From my perspective",
    "Considering the scope",
    "Having examined this",
    "Upon careful review",
    "From what I can see",
    "After discussion with the team",
    "Based on initial assessment",
]

COMMENT_OPINIONS = [
    "this is a solid proposal",
    "this looks promising",
    "this needs more work",
    "this is well thought out",
    "this requires further discussion",
    "this aligns with our goals",
    "this raises some concerns",
    "this is exactly what we need",
    "this could use some refinement",
    "this is a step in the right direction",
    "this needs clarification",
]

COMMENT_CONCERNS = [
    "you are so wrong it hurts",
    "the timeline seems tight",
    "we should consider the budget implications",
    "the resource allocation needs review",
    "dependencies aren't clearly defined",
    "we need more stakeholder input",
    "the testing strategy is unclear",
    "migration path should be documented",
    "rollback plan is missing",
    "performance impact needs assessment",
    "security considerations are important",
    "we should validate with the architecture team",
    "documentation requirements are unclear",
]

COMMENT_QUESTIONS = [
    "What's the expected timeline?",
    "Who will be responsible for implementation?",
    "Have we considered alternatives?",
    "What are the success metrics?",
    "How does this affect existing workflows?",
    "What's the estimated cost?",
    "Are there any blockers?",
    "What's the rollback strategy?",
    "How will this be tested?",
    "What about backwards compatibility?",
    "Have stakeholders been consulted?",
    "What's the maintenance plan?",
]

COMMENT_ACTIONS = [
    "I would propose you quit.",
    "Let's schedule a meeting to discuss.",
    "I'll review this in detail and follow up.",
    "We should get input from other teams.",
    "I can help with the implementation.",
    "Let me check with the management team.",
    "I'll prepare a detailed analysis.",
    "We need to document this better.",
    "Let's create a proof of concept first.",
    "I'll coordinate with the relevant stakeholders.",
    "We should break this into smaller tasks.",
]

REPLY_ACKNOWLEDGMENTS = [
    "Now get back to work.",
    "Thanks for the feedback!",
    "Good point!",
    "I appreciate your input.",
    "That's a valid concern.",
    "Great observation!",
    "Thanks for raising this.",
    "I'm glad you mentioned that.",
    "Excellent question!",
    "Fair point.",
    "You're absolutely right.",
    "Thanks for the detailed review!",
]

REPLY_RESPONSES = [
    "I've updated the proposal to address this",
    "Let me clarify that section",
    "That's already covered in the documentation",
    "I'll add more details about this",
    "We discussed this with the team and",
    "I've been working on that aspect",
    "That's on our roadmap for the next phase",
    "We can definitely include that",
    "I'll coordinate with the relevant team on this",
    "Let me investigate and get back to you",
]

REPLY_FOLLOW_UPS = [
    "You are lucky if I respond.",
    "I'll share an update by end of week.",
    "Let me know if you need more information.",
    "Feel free to reach out if you have questions.",
    "I'll schedule a follow-up meeting.",
    "We can discuss this in more detail offline.",
    "I'll prepare a detailed document.",
    "Happy to hop on a call to discuss.",
    "I'll keep you posted on progress.",
    "Let me know your thoughts on the revised version.",
    "Looking forward to your feedback.",
]

TECHNICAL_TOPICS = [
    "deleting prod",
    "force pushing master",
    "addign a bitcoin miner to the code",
    "database migration",
    "API integration",
    "authentication flow",
    "caching strategy",
    "error handling",
    "logging infrastructure",
    "monitoring setup",
    "deployment pipeline",
    "data validation",
    "permission model",
    "search functionality",
    "notification system",
    "indexing strategy",
    "backup procedures",
    "scalability concerns",
    "load balancing",
]


def generate_random_comment():
    """Generate a randomized comment with natural variation."""
    templates = [
        # Opinion-based comments
        lambda: f"{random.choice(COMMENT_STARTERS)}, {random.choice(COMMENT_OPINIONS)}. {random.choice(COMMENT_QUESTIONS)}",
        # Concern-based comments
        lambda: f"{random.choice(COMMENT_STARTERS)}, {random.choice(COMMENT_CONCERNS)}. {random.choice(COMMENT_ACTIONS)}",
        # Question-focused comments
        lambda: f"{random.choice(COMMENT_QUESTIONS)} {random.choice(COMMENT_QUESTIONS)} {random.choice(COMMENT_ACTIONS)}",
        # Technical focus
        lambda: f"Regarding the {random.choice(TECHNICAL_TOPICS)}, {random.choice(COMMENT_CONCERNS)}. {random.choice(COMMENT_QUESTIONS)}",
        # Positive with action
        lambda: f"{random.choice(COMMENT_OPINIONS).capitalize()}, but {random.choice(COMMENT_CONCERNS)}. {random.choice(COMMENT_ACTIONS)}",
        # Mixed feedback
        lambda: f"{random.choice(COMMENT_STARTERS)}, {random.choice(COMMENT_OPINIONS)} overall. However, {random.choice(COMMENT_CONCERNS)}.",
        # Short and direct
        lambda: f"{random.choice(COMMENT_OPINIONS).capitalize()}. {random.choice(COMMENT_QUESTIONS)}",
        # Detailed review
        lambda: f"{random.choice(COMMENT_STARTERS)}, {random.choice(COMMENT_OPINIONS)}. The {random.choice(TECHNICAL_TOPICS)} aspect looks good, but {random.choice(COMMENT_CONCERNS)}. {random.choice(COMMENT_ACTIONS)}",
    ]

    return random.choice(templates)()


def generate_random_reply():
    """Generate a randomized reply with natural variation."""
    templates = [
        # Acknowledgment + response
        lambda: f"{random.choice(REPLY_ACKNOWLEDGMENTS)} {random.choice(REPLY_RESPONSES)}. {random.choice(REPLY_FOLLOW_UPS)}",
        # Direct response
        lambda: f"{random.choice(REPLY_RESPONSES)} regarding {random.choice(TECHNICAL_TOPICS)}. {random.choice(REPLY_FOLLOW_UPS)}",
        # Short acknowledgment
        lambda: f"{random.choice(REPLY_ACKNOWLEDGMENTS)} {random.choice(REPLY_RESPONSES)}.",
        # Detailed response
        lambda: f"{random.choice(REPLY_ACKNOWLEDGMENTS)} {random.choice(REPLY_RESPONSES)} and also addressed the {random.choice(TECHNICAL_TOPICS)}. {random.choice(REPLY_FOLLOW_UPS)}",
        # Action-oriented
        lambda: f"{random.choice(REPLY_ACKNOWLEDGMENTS)} {random.choice(REPLY_RESPONSES)}. I'll also look into the {random.choice(TECHNICAL_TOPICS)}. {random.choice(REPLY_FOLLOW_UPS)}",
        # Clarification
        lambda: f"To clarify, {random.choice(REPLY_RESPONSES)} in the previous version. {random.choice(REPLY_FOLLOW_UPS)}",
    ]

    return random.choice(templates)()


def create_comment(request_id: str, content: str) -> dict:
    """Create a top-level comment on a request.

    Args:
        request_id: The ID of the request
        content: The comment content

    Returns:
        The created comment data or None if failed
    """
    url = f"{BASE_URL}/requests/{request_id}/comments"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {"payload": {"content": content, "format": "html"}}

    try:
        response = requests.post(url, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        print(f"✓ Created comment: {content[:50]}...")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to create comment: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"  Response: {e.response.text}")
        return None


def create_reply(request_id: str, parent_comment_id: str, content: str) -> dict:
    """Create a reply to a comment.

    Args:
        request_id: The ID of the request
        parent_comment_id: The ID of the parent comment
        content: The reply content

    Returns:
        The created reply data or None if failed
    """
    url = f"{BASE_URL}/requests/{request_id}/comments/{parent_comment_id}/reply"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {"payload": {"content": content, "format": "html"}}

    try:
        response = requests.post(url, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        print(f"  ✓ Created reply: {content[:50]}...")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"  ✗ Failed to create reply: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"    Response: {e.response.text}")
        return None


def populate_comments_and_replies(request_id: str, num_comments: int, num_replies: int):
    """Populate a request with comments and replies.

    Args:
        request_id: The ID of the request
        num_comments: Number of top-level comments to create
        num_replies: Number of replies per comment
    """
    print(f"\n{'='*70}")
    print(f"Populating Request ID: {request_id}")
    print(f"Creating {num_comments} comments with {num_replies} replies each")
    print(f"Total items: {num_comments + (num_comments * num_replies)}")
    print(f"{'='*70}\n")

    created_comments = []
    created_replies = []

    # Create top-level comments
    for i in range(num_comments):
        comment_content = generate_random_comment()

        comment = create_comment(request_id, comment_content)
        if comment:
            created_comments.append(comment)

            # Create replies to this comment
            print(f"  Creating {num_replies} replies for comment #{i+1}...")
            for j in range(num_replies):
                reply_content = generate_random_reply()

                reply = create_reply(request_id, comment["id"], reply_content)
                if reply:
                    created_replies.append(reply)

            print()  # Empty line for readability

    # Summary
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"✓ Created {len(created_comments)} top-level comments")
    print(f"✓ Created {len(created_replies)} replies")
    print(f"✓ Total: {len(created_comments) + len(created_replies)} items")
    print(f"{'='*70}\n")


def main():
    """Main function."""
    # Disable SSL warnings for local development
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    if REQUEST_ID == "YOUR_REQUEST_ID_HERE":
        print("ERROR: Please update REQUEST_ID in the script with an actual request ID")
        return

    # Populate the request
    populate_comments_and_replies(
        request_id=REQUEST_ID,
        num_comments=NUM_TOP_LEVEL_COMMENTS,
        num_replies=NUM_REPLIES_PER_COMMENT,
    )


if __name__ == "__main__":
    main()
