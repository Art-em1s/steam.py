from __future__ import annotations

from collections.abc import Mapping

import betterproto

from . import (
    chat,
    comments,
    content_server,
    econ,
    friend_messages,
    game_servers,
    inventory,
    parental,
    player,
    published_file,
    reviews,
    two_factor,
)

__all__ = ("UMS",)


UMS: Mapping[str, type[betterproto.Message]] = {
    "ChatRoom.CreateChatRoomGroup#1_Request": chat.CreateChatRoomGroupRequest,
    "ChatRoom.CreateChatRoomGroup#1_Response": chat.CreateChatRoomGroupResponse,
    "ChatRoom.SaveChatRoomGroup#1_Request": chat.SaveChatRoomGroupRequest,
    "ChatRoom.SaveChatRoomGroup#1_Response": chat.SaveChatRoomGroupResponse,
    "ChatRoom.RenameChatRoomGroup#1_Request": chat.RenameChatRoomGroupRequest,
    "ChatRoom.RenameChatRoomGroup#1_Response": chat.RenameChatRoomGroupResponse,
    "ChatRoom.SetChatRoomGroupTagline#1_Request": chat.SetChatRoomGroupTaglineRequest,
    "ChatRoom.SetChatRoomGroupTagline#1_Response": chat.SetChatRoomGroupTaglineResponse,
    "ChatRoom.SetChatRoomGroupAvatar#1_Request": chat.SetChatRoomGroupAvatarRequest,
    "ChatRoom.SetChatRoomGroupAvatar#1_Response": chat.SetChatRoomGroupAvatarResponse,
    "ChatRoom.SetChatRoomGroupWatchingBroadcast#1_Request": chat.SetChatRoomGroupWatchingBroadcastRequest,
    "ChatRoom.SetChatRoomGroupWatchingBroadcast#1_Response": chat.SetChatRoomGroupWatchingBroadcastResponse,
    "ChatRoom.JoinMiniGameForChatRoomGroup#1_Request": chat.JoinMiniGameForChatRoomGroupRequest,
    "ChatRoom.JoinMiniGameForChatRoomGroup#1_Response": chat.JoinMiniGameForChatRoomGroupResponse,
    "ChatRoom.EndMiniGameForChatRoomGroup#1_Request": chat.EndMiniGameForChatRoomGroupRequest,
    "ChatRoom.EndMiniGameForChatRoomGroup#1_Response": chat.EndMiniGameForChatRoomGroupResponse,
    "ChatRoom.MuteUserInGroup#1_Request": chat.MuteUserRequest,
    "ChatRoom.MuteUserInGroup#1_Response": chat.MuteUserResponse,
    "ChatRoom.KickUserFromGroup#1_Request": chat.KickUserRequest,
    "ChatRoom.KickUserFromGroup#1_Response": chat.KickUserResponse,
    "ChatRoom.SetUserBanState#1_Request": chat.SetUserBanStateRequest,
    "ChatRoom.SetUserBanState#1_Response": chat.SetUserBanStateResponse,
    "ChatRoom.RevokeInviteToGroup#1_Request": chat.RevokeInviteRequest,
    "ChatRoom.RevokeInviteToGroup#1_Response": chat.RevokeInviteResponse,
    "ChatRoom.CreateRole#1_Request": chat.CreateRoleRequest,
    "ChatRoom.CreateRole#1_Response": chat.CreateRoleResponse,
    "ChatRoom.GetRoles#1_Request": chat.GetRolesRequest,
    "ChatRoom.GetRoles#1_Response": chat.GetRolesResponse,
    "ChatRoom.RenameRole#1_Request": chat.RenameRoleRequest,
    "ChatRoom.RenameRole#1_Response": chat.RenameRoleResponse,
    "ChatRoom.ReorderRole#1_Request": chat.ReorderRoleRequest,
    "ChatRoom.ReorderRole#1_Response": chat.ReorderRoleResponse,
    "ChatRoom.DeleteRole#1_Request": chat.DeleteRoleRequest,
    "ChatRoom.DeleteRole#1_Response": chat.DeleteRoleResponse,
    "ChatRoom.GetRoleActions#1_Request": chat.GetRoleActionsRequest,
    "ChatRoom.GetRoleActions#1_Response": chat.GetRoleActionsResponse,
    "ChatRoom.ReplaceRoleActions#1_Request": chat.ReplaceRoleActionsRequest,
    "ChatRoom.ReplaceRoleActions#1_Response": chat.ReplaceRoleActionsResponse,
    "ChatRoom.AddRoleToUser#1_Request": chat.AddRoleToUserRequest,
    "ChatRoom.AddRoleToUser#1_Response": chat.AddRoleToUserResponse,
    "ChatRoom.GetRolesForUser#1_Request": chat.GetRolesForUserRequest,
    "ChatRoom.GetRolesForUser#1_Response": chat.GetRolesForUserResponse,
    "ChatRoom.DeleteRoleFromUser#1_Request": chat.DeleteRoleFromUserRequest,
    "ChatRoom.DeleteRoleFromUser#1_Response": chat.DeleteRoleFromUserResponse,
    "ChatRoom.JoinChatRoomGroup#1_Request": chat.JoinChatRoomGroupRequest,
    "ChatRoom.JoinChatRoomGroup#1_Response": chat.JoinChatRoomGroupResponse,
    "ChatRoom.InviteFriendToChatRoomGroup#1_Request": chat.InviteFriendToChatRoomGroupRequest,
    "ChatRoom.InviteFriendToChatRoomGroup#1_Response": chat.InviteFriendToChatRoomGroupResponse,
    "ChatRoom.LeaveChatRoomGroup#1_Request": chat.LeaveChatRoomGroupRequest,
    "ChatRoom.LeaveChatRoomGroup#1_Response": chat.LeaveChatRoomGroupResponse,
    "ChatRoom.CreateChatRoom#1_Request": chat.CreateChatRoomRequest,
    "ChatRoom.CreateChatRoom#1_Response": chat.CreateChatRoomResponse,
    "ChatRoom.DeleteChatRoom#1_Request": chat.DeleteChatRoomRequest,
    "ChatRoom.DeleteChatRoom#1_Response": chat.DeleteChatRoomResponse,
    "ChatRoom.RenameChatRoom#1_Request": chat.RenameChatRoomRequest,
    "ChatRoom.RenameChatRoom#1_Response": chat.RenameChatRoomResponse,
    "ChatRoom.ReorderChatRoom#1_Request": chat.ReorderChatRoomRequest,
    "ChatRoom.ReorderChatRoom#1_Response": chat.ReorderChatRoomResponse,
    "ChatRoom.SendChatMessage#1_Request": chat.SendChatMessageRequest,
    "ChatRoom.SendChatMessage#1_Response": chat.SendChatMessageResponse,
    "ChatRoom.JoinVoiceChat#1_Request": chat.JoinVoiceChatRequest,
    "ChatRoom.JoinVoiceChat#1_Response": chat.JoinVoiceChatResponse,
    "ChatRoom.LeaveVoiceChat#1_Request": chat.LeaveVoiceChatRequest,
    "ChatRoom.LeaveVoiceChat#1_Response": chat.LeaveVoiceChatResponse,
    "ChatRoom.GetMessageHistory#1_Request": chat.GetMessageHistoryRequest,
    "ChatRoom.GetMessageHistory#1_Response": chat.GetMessageHistoryResponse,
    "ChatRoom.GetMyChatRoomGroups#1_Request": chat.GetMyChatRoomGroupsRequest,
    "ChatRoom.GetMyChatRoomGroups#1_Response": chat.GetMyChatRoomGroupsResponse,
    "ChatRoom.GetChatRoomGroupState#1_Request": chat.GetChatRoomGroupStateRequest,
    "ChatRoom.GetChatRoomGroupState#1_Response": chat.GetChatRoomGroupStateResponse,
    "ChatRoom.GetChatRoomGroupSummary#1_Request": chat.GetChatRoomGroupSummaryRequest,
    "ChatRoom.GetChatRoomGroupSummary#1_Response": chat.GetChatRoomGroupSummaryResponse,
    "ChatRoom.SetAppChatRoomGroupForceActive#1_Request": chat.SetAppChatRoomGroupForceActiveRequest,
    "ChatRoom.SetAppChatRoomGroupForceActive#1_Response": chat.SetAppChatRoomGroupForceActiveResponse,
    "ChatRoom.SetAppChatRoomGroupStopForceActive#1_Request": chat.SetAppChatRoomGroupStopForceActiveNotification,
    "ChatRoom.AckChatMessage#1_Request": chat.AckChatMessageNotification,
    "ChatRoom.CreateInviteLink#1_Request": chat.CreateInviteLinkRequest,
    "ChatRoom.CreateInviteLink#1_Response": chat.CreateInviteLinkResponse,
    "ChatRoom.GetInviteLinkInfo#1_Request": chat.GetInviteLinkInfoRequest,
    "ChatRoom.GetInviteLinkInfo#1_Response": chat.GetInviteLinkInfoResponse,
    "ChatRoom.GetInviteInfo#1_Request": chat.GetInviteInfoRequest,
    "ChatRoom.GetInviteInfo#1_Response": chat.GetInviteInfoResponse,
    "ChatRoom.GetInviteLinksForGroup#1_Request": chat.GetInviteLinksForGroupRequest,
    "ChatRoom.GetInviteLinksForGroup#1_Response": chat.GetInviteLinksForGroupResponse,
    "ChatRoom.GetBanList#1_Request": chat.GetBanListRequest,
    "ChatRoom.GetBanList#1_Response": chat.GetBanListResponse,
    "ChatRoom.GetInviteList#1_Request": chat.GetInviteListRequest,
    "ChatRoom.GetInviteList#1_Response": chat.GetInviteListResponse,
    "ChatRoom.DeleteInviteLink#1_Request": chat.DeleteInviteLinkRequest,
    "ChatRoom.DeleteInviteLink#1_Response": chat.DeleteInviteLinkResponse,
    "ChatRoom.SetSessionActiveChatRoomGroups#1_Request": chat.SetSessionActiveChatRoomGroupsRequest,
    "ChatRoom.SetSessionActiveChatRoomGroups#1_Response": chat.SetSessionActiveChatRoomGroupsResponse,
    "ChatRoom.SetUserChatGroupPreferences#1_Request": chat.SetUserChatGroupPreferencesRequest,
    "ChatRoom.SetUserChatGroupPreferences#1_Response": chat.SetUserChatGroupPreferencesResponse,
    "ChatRoom.DeleteChatMessages#1_Request": chat.DeleteChatMessagesRequest,
    "ChatRoom.DeleteChatMessages#1_Response": chat.DeleteChatMessagesResponse,
    "ChatRoom.UpdateMemberListView#1_Request": chat.UpdateMemberListViewNotification,
    "ChatRoom.SearchMembers#1_Request": chat.SearchMembersRequest,
    "ChatRoom.SearchMembers#1_Response": chat.SearchMembersResponse,
    "ChatRoom.UpdateMessageReaction#1_Request": chat.UpdateMessageReactionRequest,
    "ChatRoom.UpdateMessageReaction#1_Response": chat.UpdateMessageReactionResponse,
    "ChatRoom.GetMessageReactionReactors#1_Request": chat.GetMessageReactionReactorsRequest,
    "ChatRoom.GetMessageReactionReactors#1_Response": chat.GetMessageReactionReactorsResponse,
    "ClanChatRooms.GetClanChatRoomInfo#1_Request": chat.GetClanChatRoomInfoRequest,
    "ClanChatRooms.GetClanChatRoomInfo#1_Response": chat.GetClanChatRoomInfoResponse,
    "ClanChatRooms.SetClanChatRoomPrivate#1_Request": chat.SetClanChatRoomPrivateRequest,
    "ClanChatRooms.SetClanChatRoomPrivate#1_Response": chat.SetClanChatRoomPrivateResponse,
    "ChatRoomClient.NotifyIncomingChatMessage#1_Request": chat.IncomingChatMessageNotification,
    "ChatRoomClient.NotifyChatMessageModified#1_Request": chat.ChatMessageModifiedNotification,
    "ChatRoomClient.NotifyMemberStateChange#1_Request": chat.MemberStateChangeNotification,
    "ChatRoomClient.NotifyChatRoomHeaderStateChange#1_Request": chat.ChatRoomHeaderStateNotification,
    "ChatRoomClient.NotifyChatRoomGroupRoomsChange#1_Request": chat.ChatRoomGroupRoomsChangeNotification,
    "ChatRoomClient.NotifyShouldRejoinChatRoomVoiceChat#1_Request": chat.NotifyShouldRejoinChatRoomVoiceChatNotification,
    "ChatRoomClient.NotifyChatGroupUserStateChanged#1_Request": chat.NotifyChatGroupUserStateChangedNotification,
    "ChatRoomClient.NotifyAckChatMessageEcho#1_Request": chat.AckChatMessageNotification,
    "ChatRoomClient.NotifyChatRoomDisconnect#1_Request": chat.NotifyChatRoomDisconnectNotification,
    "ChatRoomClient.NotifyMemberListViewUpdated#1_Request": chat.MemberListViewUpdatedNotification,
    "ChatRoomClient.NotifyMessageReaction#1_Request": chat.MessageReactionNotification,
    "ContentServerDirectory.GetServersForSteamPipe#1_Request": content_server.GetServersForSteamPipeRequest,
    "ContentServerDirectory.GetServersForSteamPipe#1_Response": content_server.GetServersForSteamPipeResponse,
    "ContentServerDirectory.GetDepotPatchInfo#1_Request": content_server.GetDepotPatchInfoRequest,
    "ContentServerDirectory.GetDepotPatchInfo#1_Response": content_server.GetDepotPatchInfoResponse,
    "ContentServerDirectory.GetClientUpdateHosts#1_Request": content_server.GetClientUpdateHostsRequest,
    "ContentServerDirectory.GetClientUpdateHosts#1_Response": content_server.GetClientUpdateHostsResponse,
    "Community.GetCommentThread#1_Request": comments.CommentThreadRequest,
    "Community.GetCommentThread#1_Response": comments.CommentThreadResponse,
    "Community.PostCommentToThread#1_Request": comments.PostCommentToThreadRequest,
    "Community.PostCommentToThread#1_Response": comments.PostCommentToThreadResponse,
    "Community.DeleteCommentFromThread#1_Request": comments.DeleteCommentFromThreadRequest,
    "Community.DeleteCommentFromThread#1_Response": comments.DeleteCommentFromThreadResponse,
    "Community.RateCommentThread#1_Request": comments.RateCommentThreadRequest,
    "Community.RateCommentThread#1_Response": comments.RateCommentThreadResponse,
    "Econ.GetTradeOfferAccessToken#1_Request": econ.GetTradeOfferAccessTokenRequest,
    "Econ.GetTradeOfferAccessToken#1_Response": econ.GetTradeOfferAccessTokenResponse,
    "Econ.ClientGetItemShopOverlayAuthURL#1_Request": econ.GetItemShopOverlayAuthUrlRequest,
    "Econ.ClientGetItemShopOverlayAuthURL#1_Response": econ.GetItemShopOverlayAuthUrlResponse,
    "Econ.GetAssetClassInfo#1_Request": econ.GetAssetClassInfoRequest,
    "Econ.GetAssetClassInfo#1_Response": econ.GetAssetClassInfoResponse,
    "FriendMessages.GetRecentMessages#1_Request": friend_messages.GetRecentMessagesRequest,
    "FriendMessages.GetRecentMessages#1_Response": friend_messages.GetRecentMessagesResponse,
    "FriendMessages.GetActiveMessageSessions#1_Request": friend_messages.GetActiveMessageSessionsRequest,
    "FriendMessages.GetActiveMessageSessions#1_Response": friend_messages.GetActiveMessageSessionsResponse,
    "FriendMessages.SendMessage#1_Request": friend_messages.SendMessageRequest,
    "FriendMessages.SendMessage#1_Response": friend_messages.SendMessageResponse,
    "FriendMessages.AckMessage#1_Request": friend_messages.AckMessageNotification,
    "FriendMessages.UpdateMessageReaction#1_Request": friend_messages.UpdateMessageReactionRequest,
    "FriendMessages.UpdateMessageReaction#1_Response": friend_messages.UpdateMessageReactionResponse,
    "FriendMessagesClient.IncomingMessage#1_Request": friend_messages.IncomingMessageNotification,
    "FriendMessagesClient.NotifyAckMessageEcho#1_Request": friend_messages.AckMessageNotification,
    "FriendMessagesClient.MessageReaction#1_Request": friend_messages.MessageReactionNotification,
    "GameServers.GetServerList#1_Request": game_servers.GetServerListRequest,
    "GameServers.GetServerList#1_Response": game_servers.GetServerListResponse,
    "GameServers.GetServerSteamIDsByIP#1_Request": game_servers.GetServerSteamIDsByIpRequest,
    "GameServers.GetServerSteamIDsByIP#1_Response": game_servers.IPsWithSteamIDsResponse,
    "GameServers.GetServerIPsBySteamID#1_Request": game_servers.GetServerIPsBySteamIdRequest,
    "GameServers.GetServerIPsBySteamID#1_Response": game_servers.IPsWithSteamIDsResponse,
    "Inventory.GetInventory#1_Request": inventory.GetInventoryRequest,
    "Inventory.GetInventory#1_Response": inventory.Response,
    "Inventory.ExchangeItem#1_Request": inventory.ExchangeItemRequest,
    "Inventory.ExchangeItem#1_Response": inventory.Response,
    "Inventory.GetEligiblePromoItemDefIDs#1_Request": inventory.GetEligiblePromoItemDefIDsRequest,
    "Inventory.GetEligiblePromoItemDefIDs#1_Response": inventory.GetEligiblePromoItemDefIDsResponse,
    "Inventory.AddPromoItem#1_Request": inventory.AddItemRequest,
    "Inventory.AddPromoItem#1_Response": inventory.Response,
    "Inventory.SafeModifyItems#1_Request": inventory.ModifyItemsRequest,
    "Inventory.SafeModifyItems#1_Response": inventory.Response,
    "Inventory.ConsumePlaytime#1_Request": inventory.ConsumePlaytimeRequest,
    "Inventory.ConsumePlaytime#1_Response": inventory.Response,
    "Inventory.ConsumeItem#1_Request": inventory.ConsumeItemRequest,
    "Inventory.ConsumeItem#1_Response": inventory.Response,
    "Inventory.DevGenerateItem#1_Request": inventory.AddItemRequest,
    "Inventory.DevGenerateItem#1_Response": inventory.Response,
    "Inventory.DevSetNextDrop#1_Request": inventory.DevSetNextDropRequest,
    "Inventory.DevSetNextDrop#1_Response": inventory.Response,
    "Inventory.SplitItemStack#1_Request": inventory.SplitItemStackRequest,
    "Inventory.SplitItemStack#1_Response": inventory.Response,
    "Inventory.CombineItemStacks#1_Request": inventory.CombineItemStacksRequest,
    "Inventory.CombineItemStacks#1_Response": inventory.Response,
    "Inventory.GetItemDefMeta#1_Request": inventory.GetItemDefMetaRequest,
    "Inventory.GetItemDefMeta#1_Response": inventory.GetItemDefMetaResponse,
    "Inventory.GetUserPurchaseInfo#1_Request": inventory.GetUserPurchaseInfoRequest,
    "Inventory.GetUserPurchaseInfo#1_Response": inventory.GetUserPurchaseInfoResponse,
    "Inventory.PurchaseInit#1_Request": inventory.PurchaseInitRequest,
    "Inventory.PurchaseInit#1_Response": inventory.PurchaseInitResponse,
    "Inventory.PurchaseFinalize#1_Request": inventory.PurchaseFinalizeRequest,
    "Inventory.PurchaseFinalize#1_Response": inventory.Response,
    "Inventory.InspectItem#1_Request": inventory.InspectItemRequest,
    "Inventory.InspectItem#1_Response": inventory.Response,
    "InventoryClient.NotifyNewItems#1_Request": inventory.ClientNewItemsNotification,
    "Parental.EnableParentalSettings#1_Request": parental.EnableParentalSettingsRequest,
    "Parental.EnableParentalSettings#1_Response": parental.EnableParentalSettingsResponse,
    "Parental.DisableParentalSettings#1_Request": parental.DisableParentalSettingsRequest,
    "Parental.DisableParentalSettings#1_Response": parental.DisableParentalSettingsResponse,
    "Parental.GetParentalSettings#1_Request": parental.GetParentalSettingsRequest,
    "Parental.GetParentalSettings#1_Response": parental.GetParentalSettingsResponse,
    "Parental.GetSignedParentalSettings#1_Request": parental.GetSignedParentalSettingsRequest,
    "Parental.GetSignedParentalSettings#1_Response": parental.GetSignedParentalSettingsResponse,
    "Parental.SetParentalSettings#1_Request": parental.SetParentalSettingsRequest,
    "Parental.SetParentalSettings#1_Response": parental.SetParentalSettingsResponse,
    "Parental.ValidateToken#1_Request": parental.ValidateTokenRequest,
    "Parental.ValidateToken#1_Response": parental.ValidateTokenResponse,
    "Parental.ValidatePassword#1_Request": parental.ValidatePasswordRequest,
    "Parental.ValidatePassword#1_Response": parental.ValidatePasswordResponse,
    "Parental.LockClient#1_Request": parental.LockClientRequest,
    "Parental.LockClient#1_Response": parental.LockClientResponse,
    "Parental.RequestRecoveryCode#1_Request": parental.RequestRecoveryCodeRequest,
    "Parental.RequestRecoveryCode#1_Response": parental.RequestRecoveryCodeResponse,
    "Parental.DisableWithRecoveryCode#1_Request": parental.DisableWithRecoveryCodeRequest,
    "Parental.DisableWithRecoveryCode#1_Response": parental.DisableWithRecoveryCodeResponse,
    "Player.GetMutualFriendsForIncomingInvites#1_Request": player.GetMutualFriendsForIncomingInvitesRequest,
    "Player.GetMutualFriendsForIncomingInvites#1_Response": player.GetMutualFriendsForIncomingInvitesResponse,
    "Player.GetOwnedGames#1_Request": player.GetOwnedGamesRequest,
    "Player.GetOwnedGames#1_Response": player.GetOwnedGamesResponse,
    "Player.GetPlayNext#1_Request": player.GetPlayNextRequest,
    "Player.GetPlayNext#1_Response": player.GetPlayNextResponse,
    "Player.GetFriendsGameplayInfo#1_Request": player.GetFriendsGameplayInfoRequest,
    "Player.GetFriendsGameplayInfo#1_Response": player.GetFriendsGameplayInfoResponse,
    "Player.GetFriendsAppsActivity#1_Request": player.GetFriendsAppsActivityRequest,
    "Player.GetFriendsAppsActivity#1_Response": player.GetFriendsAppsActivityResponse,
    "Player.GetGameBadgeLevels#1_Request": player.GetGameBadgeLevelsRequest,
    "Player.GetGameBadgeLevels#1_Response": player.GetGameBadgeLevelsResponse,
    "Player.GetProfileBackground#1_Request": player.GetProfileBackgroundRequest,
    "Player.GetProfileBackground#1_Response": player.GetProfileBackgroundResponse,
    "Player.SetProfileBackground#1_Request": player.SetProfileBackgroundRequest,
    "Player.SetProfileBackground#1_Response": player.SetProfileBackgroundResponse,
    "Player.GetMiniProfileBackground#1_Request": player.GetMiniProfileBackgroundRequest,
    "Player.GetMiniProfileBackground#1_Response": player.GetMiniProfileBackgroundResponse,
    "Player.SetMiniProfileBackground#1_Request": player.SetMiniProfileBackgroundRequest,
    "Player.SetMiniProfileBackground#1_Response": player.SetMiniProfileBackgroundResponse,
    "Player.GetAvatarFrame#1_Request": player.GetAvatarFrameRequest,
    "Player.GetAvatarFrame#1_Response": player.GetAvatarFrameResponse,
    "Player.SetAvatarFrame#1_Request": player.SetAvatarFrameRequest,
    "Player.SetAvatarFrame#1_Response": player.SetAvatarFrameResponse,
    "Player.GetAnimatedAvatar#1_Request": player.GetAnimatedAvatarRequest,
    "Player.GetAnimatedAvatar#1_Response": player.GetAnimatedAvatarResponse,
    "Player.SetAnimatedAvatar#1_Request": player.SetAnimatedAvatarRequest,
    "Player.SetAnimatedAvatar#1_Response": player.SetAnimatedAvatarResponse,
    "Player.GetProfileItemsOwned#1_Request": player.GetProfileItemsOwnedRequest,
    "Player.GetProfileItemsOwned#1_Response": player.GetProfileItemsOwnedResponse,
    "Player.GetProfileItemsEquipped#1_Request": player.GetProfileItemsEquippedRequest,
    "Player.GetProfileItemsEquipped#1_Response": player.GetProfileItemsEquippedResponse,
    "Player.SetEquippedProfileItemFlags#1_Request": player.SetEquippedProfileItemFlagsRequest,
    "Player.SetEquippedProfileItemFlags#1_Response": player.SetEquippedProfileItemFlagsResponse,
    "Player.GetEmoticonList#1_Request": player.GetEmoticonListRequest,
    "Player.GetEmoticonList#1_Response": player.GetEmoticonListResponse,
    "Player.GetAchievementsProgress#1_Request": player.GetAchievementsProgressRequest,
    "Player.GetAchievementsProgress#1_Response": player.GetAchievementsProgressResponse,
    "Player.GetFavoriteBadge#1_Request": player.GetFavoriteBadgeRequest,
    "Player.GetFavoriteBadge#1_Response": player.GetFavoriteBadgeResponse,
    "Player.SetFavoriteBadge#1_Request": player.SetFavoriteBadgeRequest,
    "Player.SetFavoriteBadge#1_Response": player.SetFavoriteBadgeResponse,
    "Player.GetProfileCustomization#1_Request": player.GetProfileCustomizationRequest,
    "Player.GetProfileCustomization#1_Response": player.GetProfileCustomizationResponse,
    "Player.GetPurchasedProfileCustomizations#1_Request": player.GetPurchasedProfileCustomizationsRequest,
    "Player.GetPurchasedProfileCustomizations#1_Response": player.GetPurchasedProfileCustomizationsResponse,
    "Player.GetPurchasedAndUpgradedProfileCustomizations#1_Request": player.GetPurchasedAndUpgradedProfileCustomizationsRequest,
    "Player.GetPurchasedAndUpgradedProfileCustomizations#1_Response": player.GetPurchasedAndUpgradedProfileCustomizationsResponse,
    "Player.GetProfileThemesAvailable#1_Request": player.GetProfileThemesAvailableRequest,
    "Player.GetProfileThemesAvailable#1_Response": player.GetProfileThemesAvailableResponse,
    "Player.SetProfileTheme#1_Request": player.SetProfileThemeRequest,
    "Player.SetProfileTheme#1_Response": player.SetProfileThemeResponse,
    "Player.SetProfilePreferences#1_Request": player.SetProfilePreferencesRequest,
    "Player.SetProfilePreferences#1_Response": player.SetProfilePreferencesResponse,
    "Player.PostStatusToFriends#1_Request": player.PostStatusToFriendsRequest,
    "Player.PostStatusToFriends#1_Response": player.PostStatusToFriendsResponse,
    "Player.GetPostedStatus#1_Request": player.GetPostedStatusRequest,
    "Player.GetPostedStatus#1_Response": player.GetPostedStatusResponse,
    "Player.DeletePostedStatus#1_Request": player.DeletePostedStatusRequest,
    "Player.DeletePostedStatus#1_Response": player.DeletePostedStatusResponse,
    "Player.ClientGetLastPlayedTimes#1_Request": player.GetLastPlayedTimesRequest,
    "Player.ClientGetLastPlayedTimes#1_Response": player.GetLastPlayedTimesResponse,
    "Player.AcceptSSA#1_Request": player.AcceptSsaRequest,
    "Player.AcceptSSA#1_Response": player.AcceptSsaResponse,
    "Player.GetNicknameList#1_Request": player.GetNicknameListRequest,
    "Player.GetNicknameList#1_Response": player.GetNicknameListResponse,
    "Player.GetPerFriendPreferences#1_Request": player.GetPerFriendPreferencesRequest,
    "Player.GetPerFriendPreferences#1_Response": player.GetPerFriendPreferencesResponse,
    "Player.SetPerFriendPreferences#1_Request": player.SetPerFriendPreferencesRequest,
    "Player.SetPerFriendPreferences#1_Response": player.SetPerFriendPreferencesResponse,
    "Player.AddFriend#1_Request": player.AddFriendRequest,
    "Player.AddFriend#1_Response": player.AddFriendResponse,
    "Player.RemoveFriend#1_Request": player.RemoveFriendRequest,
    "Player.RemoveFriend#1_Response": player.RemoveFriendResponse,
    "Player.IgnoreFriend#1_Request": player.IgnoreFriendRequest,
    "Player.IgnoreFriend#1_Response": player.IgnoreFriendResponse,
    "Player.GetCommunityPreferences#1_Request": player.GetCommunityPreferencesRequest,
    "Player.GetCommunityPreferences#1_Response": player.GetCommunityPreferencesResponse,
    "Player.SetCommunityPreferences#1_Request": player.SetCommunityPreferencesRequest,
    "Player.SetCommunityPreferences#1_Response": player.SetCommunityPreferencesResponse,
    "Player.GetTextFilterWords#1_Request": player.GetTextFilterWordsRequest,
    "Player.GetTextFilterWords#1_Response": player.GetTextFilterWordsResponse,
    "Player.GetNewSteamAnnouncementState#1_Request": player.GetNewSteamAnnouncementStateRequest,
    "Player.GetNewSteamAnnouncementState#1_Response": player.GetNewSteamAnnouncementStateResponse,
    "Player.UpdateSteamAnnouncementLastRead#1_Request": player.UpdateSteamAnnouncementLastReadRequest,
    "Player.UpdateSteamAnnouncementLastRead#1_Response": player.UpdateSteamAnnouncementLastReadResponse,
    "Player.GetPrivacySettings#1_Request": player.GetPrivacySettingsRequest,
    "Player.GetPrivacySettings#1_Response": player.GetPrivacySettingsResponse,
    "Player.GetDurationControl#1_Request": player.GetDurationControlRequest,
    "Player.GetDurationControl#1_Response": player.GetDurationControlResponse,
    "PublishedFile.Subscribe#1_Request": published_file.SubscribeRequest,
    "PublishedFile.Subscribe#1_Response": published_file.SubscribeResponse,
    "PublishedFile.Unsubscribe#1_Request": published_file.UnsubscribeRequest,
    "PublishedFile.Unsubscribe#1_Response": published_file.UnsubscribeResponse,
    "PublishedFile.CanSubscribe#1_Request": published_file.CanSubscribeRequest,
    "PublishedFile.CanSubscribe#1_Response": published_file.CanSubscribeResponse,
    "PublishedFile.Publish#1_Request": published_file.PublishRequest,
    "PublishedFile.Publish#1_Response": published_file.PublishResponse,
    "PublishedFile.GetDetails#1_Request": published_file.GetDetailsRequest,
    "PublishedFile.GetDetails#1_Response": published_file.GetDetailsResponse,
    "PublishedFile.GetItemInfo#1_Request": published_file.GetItemInfoRequest,
    "PublishedFile.GetItemInfo#1_Response": published_file.GetItemInfoResponse,
    "PublishedFile.GetUserFiles#1_Request": published_file.GetUserFilesRequest,
    "PublishedFile.GetUserFiles#1_Response": published_file.GetUserFilesResponse,
    "PublishedFile.AreFilesInSubscriptionList#1_Request": published_file.AreFilesInSubscriptionListRequest,
    "PublishedFile.AreFilesInSubscriptionList#1_Response": published_file.AreFilesInSubscriptionListResponse,
    "PublishedFile.Update#1_Request": published_file.UpdateRequest,
    "PublishedFile.Update#1_Response": published_file.UpdateResponse,
    "PublishedFile.GetChangeHistoryEntry#1_Request": published_file.GetChangeHistoryEntryRequest,
    "PublishedFile.GetChangeHistoryEntry#1_Response": published_file.GetChangeHistoryEntryResponse,
    "PublishedFile.GetChangeHistory#1_Request": published_file.GetChangeHistoryRequest,
    "PublishedFile.GetChangeHistory#1_Response": published_file.GetChangeHistoryResponse,
    "PublishedFile.RefreshVotingQueue#1_Request": published_file.RefreshVotingQueueRequest,
    "PublishedFile.RefreshVotingQueue#1_Response": published_file.RefreshVotingQueueResponse,
    "PublishedFile.QueryFiles#1_Request": published_file.QueryFilesRequest,
    "PublishedFile.QueryFiles#1_Response": published_file.QueryFilesResponse,
    "PublishedFile.AddAppRelationship#1_Request": published_file.AddAppRelationshipRequest,
    "PublishedFile.AddAppRelationship#1_Response": published_file.AddAppRelationshipResponse,
    "PublishedFile.RemoveAppRelationship#1_Request": published_file.RemoveAppRelationshipRequest,
    "PublishedFile.RemoveAppRelationship#1_Response": published_file.RemoveAppRelationshipResponse,
    "PublishedFile.GetAppRelationships#1_Request": published_file.GetAppRelationshipsRequest,
    "PublishedFile.GetAppRelationships#1_Response": published_file.GetAppRelationshipsResponse,
    "PublishedFile.StartPlaytimeTracking#1_Request": published_file.StartPlaytimeTrackingRequest,
    "PublishedFile.StartPlaytimeTracking#1_Response": published_file.StartPlaytimeTrackingResponse,
    "PublishedFile.StopPlaytimeTracking#1_Request": published_file.StopPlaytimeTrackingRequest,
    "PublishedFile.StopPlaytimeTracking#1_Response": published_file.StopPlaytimeTrackingResponse,
    "PublishedFile.StopPlaytimeTrackingForAllAppItems#1_Request": published_file.StopPlaytimeTrackingForAllAppItemsRequest,
    "PublishedFile.StopPlaytimeTrackingForAllAppItems#1_Response": published_file.StopPlaytimeTrackingForAllAppItemsResponse,
    "PublishedFile.SetPlaytimeForControllerConfigs#1_Request": published_file.SetPlaytimeForControllerConfigsRequest,
    "PublishedFile.SetPlaytimeForControllerConfigs#1_Response": published_file.SetPlaytimeForControllerConfigsResponse,
    "PublishedFile.AddChild#1_Request": published_file.AddChildRequest,
    "PublishedFile.AddChild#1_Response": published_file.AddChildResponse,
    "PublishedFile.RemoveChild#1_Request": published_file.RemoveChildRequest,
    "PublishedFile.RemoveChild#1_Response": published_file.RemoveChildResponse,
    "PublishedFile.GetUserVoteSummary#1_Request": published_file.GetUserVoteSummaryRequest,
    "PublishedFile.GetUserVoteSummary#1_Response": published_file.GetUserVoteSummaryResponse,
    "PublishedFile.GetItemChanges#1_Request": published_file.GetItemChangesRequest,
    "PublishedFile.GetItemChanges#1_Response": published_file.GetItemChangesResponse,
    "TwoFactor.QueryStatus#1_Request": two_factor.StatusRequest,
    "TwoFactor.QueryStatus#1_Response": two_factor.StatusResponse,
    "TwoFactor.AddAuthenticator#1_Request": two_factor.AddAuthenticatorRequest,
    "TwoFactor.AddAuthenticator#1_Response": two_factor.AddAuthenticatorResponse,
    "TwoFactor.SendEmail#1_Request": two_factor.SendEmailRequest,
    "TwoFactor.SendEmail#1_Response": two_factor.SendEmailResponse,
    "TwoFactor.FinalizeAddAuthenticator#1_Request": two_factor.FinalizeAddAuthenticatorRequest,
    "TwoFactor.FinalizeAddAuthenticator#1_Response": two_factor.FinalizeAddAuthenticatorResponse,
    "TwoFactor.RemoveAuthenticator#1_Request": two_factor.RemoveAuthenticatorRequest,
    "TwoFactor.RemoveAuthenticator#1_Response": two_factor.RemoveAuthenticatorResponse,
    "TwoFactor.CreateEmergencyCodes#1_Request": two_factor.CreateEmergencyCodesRequest,
    "TwoFactor.CreateEmergencyCodes#1_Response": two_factor.CreateEmergencyCodesResponse,
    "TwoFactor.DestroyEmergencyCodes#1_Request": two_factor.DestroyEmergencyCodesRequest,
    "TwoFactor.DestroyEmergencyCodes#1_Response": two_factor.DestroyEmergencyCodesResponse,
    "TwoFactor.ValidateToken#1_Request": two_factor.ValidateTokenRequest,
    "TwoFactor.ValidateToken#1_Response": two_factor.ValidateTokenResponse,
    "UserReviews.Update#1_Request": reviews.UpdateRequest,
    "UserReviews.Update#1_Response": reviews.UpdateResponse,
    "UserReviews.GetIndividualRecommendations#1_Request": reviews.GetIndividualRecommendationsRequest,
    "UserReviews.GetIndividualRecommendations#1_Response": reviews.GetIndividualRecommendationsResponse,
}
