from .models import *
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    """
    研究方向模型序列化
    """

    class Meta:
        model = SubjectModel
        fields = "__all__"


class ContributionTypeSerializer(serializers.ModelSerializer):
    """
    投稿类型模型序列化
    """

    class Meta:
        model = ContributionTypeModel
        fields = "__all__"


class TradeSerializer(serializers.ModelSerializer):
    """
    行业领域模型序列化
    """

    class Meta:
        model = TradeModel
        fields = "__all__"


class CheckManuscriptSerializer(serializers.ModelSerializer):
    """
    稿件检测模型序列化
    """

    class Meta:
        model = CheckManuscriptModel
        fields = "__all__"


class ReviewManuscriptSerializer(serializers.ModelSerializer):
    """
    稿件审核模型序列化
    """

    class Meta:
        model = ReviewManuscriptModel
        fields = "__all__"


class ManuscriptSerializer(serializers.ModelSerializer):
    """
    稿件信息模型序列化
    """
    check_status = CheckManuscriptSerializer()
    review_status = ReviewManuscriptSerializer()

    class Meta:
        model = ReviewManuscriptModel
        fields = "__all__"

    def create(self, validated_data):
        """
        重写create方法，将获取的稿件数据存储到对应的数据表中
        :param validated_data:
        :return:
        """
        check_status = validated_data.get("check_status", None)
        review_status = validated_data.get("review_status", None)
        check_id = check_status.get("id", None)
        review_id = review_status.get("id", None)
        isCheck = CheckManuscriptModel.objects.filter(id=check_id).first()  #查看稿件审核记录表中是否存在有记录，没有则生成对应记录
        isReview = ReviewManuscriptModel.objects.filter(id=review_id).first()
        # nowTime = datetime.now()
        if not isCheck:
            # newCheckID = "CH" + str(nowTime.year) + str(nowTime.month) + str(nowTime.day) + str(nowTime.hour) + str(
            #     nowTime.minute) + str(nowTime.second)
            isCheck =CheckManuscriptModel.objects.create(**check_status)
        if not isReview:
            isReview=ReviewManuscriptModel.objects.create(**review_status)
        newManuscriptData=validated_data
        newManuscriptData['check_status']=isCheck
        newManuscriptData['review_status']=isReview
        return ManuscriptModel.objects.create(**newManuscriptData)

    def update(self, instance, validated_data):
        """
        更新稿件信息
        :param instance:
        :param validated_data:
        :return:
        """
        check_status = validated_data.get("check_status", None)
        review_status = validated_data.get("review_status", None)
        check_id = check_status.get("id", None)
        review_id = review_status.get("id", None)
        isCheck = CheckManuscriptModel.objects.filter(id=check_id).first()  # 查看稿件审核记录表中是否存在有记录，没有则生成对应记录
        isReview = ReviewManuscriptModel.objects.filter(id=review_id).first()
        updateManuscriptData=validated_data
        if isCheck and isReview:
            isCheck.update(**check_status)
            isReview.update(**review_status)
            manuscript_id=validated_data.get("manuscript_id",None)
            updateManuscriptData['check_status']=isCheck
            updateManuscriptData['review_status']=isReview
            return ManuscriptModel.objects.filter(manuscript_id=manuscript_id).update(**updateManuscriptData)
        elif not isCheck and isReview:
            isReview.update(**review_status)
            manuscript_id = validated_data.get("manuscript_id", None)
            updateManuscriptData['review_status'] = isReview
            return ManuscriptModel.objects.filter(manuscript_id=manuscript_id).update(**updateManuscriptData)
        elif isCheck and not isReview:
            isCheck.update(**check_status)
            manuscript_id = validated_data.get("manuscript_id", None)
            updateManuscriptData['check_status']=isCheck
            return ManuscriptModel.objects.filter(manuscript_id=manuscript_id).update(**updateManuscriptData)



