import numpy as np

def user_collaborative_filtering(user_item_matrix, target_user_id, k=5):
    # 计算目标用户与其他用户之间的相似度
    similarities = {}
    target_user_ratings = user_item_matrix[target_user_id]
    for user_id, ratings in enumerate(user_item_matrix):
        if user_id == target_user_id:
            continue
        common_items = np.logical_and(target_user_ratings > 0, ratings > 0)
        if np.sum(common_items) > 0:
            similarity = np.dot(target_user_ratings, ratings) / (np.linalg.norm(target_user_ratings) * np.linalg.norm(ratings))
            similarities[user_id] = similarity
    
    # 找到与目标用户相似度最高的K个用户
    similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]
    
    # 生成推荐列表
    recommendation = {}
    for item_id in range(len(target_user_ratings)):
        if target_user_ratings[item_id] == 0:
            numerator = 0
            denominator = 0
            for user, similarity in similar_users:
                if user_item_matrix[user, item_id] > 0:
                    numerator += similarity * user_item_matrix[user, item_id]
                    denominator += abs(similarity)
            if denominator > 0:
                recommendation[item_id] = numerator / denominator
    
    # 按照推荐评分排序并返回推荐列表
    sorted_recommendation = sorted(recommendation.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendation

# 示例数据
user_item_matrix = np.array([
    [5, 4, 0, 0, 0],
    [0, 0, 3, 4, 0],
    [0, 0, 0, 0, 5],
    [4, 0, 0, 0, 0],
])

# 目标用户ID为0，寻找与目标用户相似的5个用户并进行推荐
target_user_id = 0
recommended_items = user_collaborative_filtering(user_item_matrix, target_user_id, k=5)
print("推荐列表：", recommended_items)
