# coding: utf-8

# flake8: noqa

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "2019.2"

# import apis into sdk package
from allegro_api.api.additional_services_api import AdditionalServicesApi
from allegro_api.api.after_sale_services_api import AfterSaleServicesApi
from allegro_api.api.batch_offer_modification_api import BatchOfferModificationApi
from allegro_api.api.categories_and_parameters_api import CategoriesAndParametersApi
from allegro_api.api.contacts_api import ContactsApi
from allegro_api.api.delivery_api import DeliveryApi
from allegro_api.api.disputes_api import DisputesApi
from allegro_api.api.images_and_attachments_api import ImagesAndAttachmentsApi
from allegro_api.api.listing_badges_api import ListingBadgesApi
from allegro_api.api.offer_management_api import OfferManagementApi
from allegro_api.api.offer_tags_api import OfferTagsApi
from allegro_api.api.offer_variants_api import OfferVariantsApi
from allegro_api.api.order_management_api import OrderManagementApi
from allegro_api.api.points_of_service_api import PointsOfServiceApi
from allegro_api.api.pricing_api import PricingApi
from allegro_api.api.products_api import ProductsApi
from allegro_api.api.public_offer_information_api import PublicOfferInformationApi
from allegro_api.api.public_user_information_api import PublicUserInformationApi
from allegro_api.api.sets_and_rebates_api import SetsAndRebatesApi
from allegro_api.api.size_tables_api import SizeTablesApi
from allegro_api.api.user_information_api import UserInformationApi
from allegro_api.api.users_offer_information_api import UsersOfferInformationApi

# import ApiClient
from allegro_api.api_client import ApiClient
from allegro_api.configuration import Configuration
# import models into sdk package
from allegro_api.models.additional_service_definition_request import AdditionalServiceDefinitionRequest
from allegro_api.models.additional_service_request import AdditionalServiceRequest
from allegro_api.models.additional_service_response import AdditionalServiceResponse
from allegro_api.models.additional_services_group import AdditionalServicesGroup
from allegro_api.models.additional_services_group_request import AdditionalServicesGroupRequest
from allegro_api.models.additional_services_group_response import AdditionalServicesGroupResponse
from allegro_api.models.additional_services_groups import AdditionalServicesGroups
from allegro_api.models.address import Address
from allegro_api.models.after_sales_services import AfterSalesServices
from allegro_api.models.answer import Answer
from allegro_api.models.attachment_declaration import AttachmentDeclaration
from allegro_api.models.attachment_file import AttachmentFile
from allegro_api.models.attachment_file_request import AttachmentFileRequest
from allegro_api.models.attachment_type import AttachmentType
from allegro_api.models.available_constraint import AvailableConstraint
from allegro_api.models.average_rates import AverageRates
from allegro_api.models.basic_definition_response import BasicDefinitionResponse
from allegro_api.models.benefit import Benefit
from allegro_api.models.benefit_specification import BenefitSpecification
from allegro_api.models.buyer_reference import BuyerReference
from allegro_api.models.campaign_request_dto import CampaignRequestDto
from allegro_api.models.campaign_response_dto import CampaignResponseDto
from allegro_api.models.caption import Caption
from allegro_api.models.categories_dto import CategoriesDto
from allegro_api.models.category import Category
from allegro_api.models.category_dto import CategoryDto
from allegro_api.models.category_id_dto import CategoryIdDto
from allegro_api.models.category_options_dto import CategoryOptionsDto
from allegro_api.models.category_parameter import CategoryParameter
from allegro_api.models.category_parameter_list import CategoryParameterList
from allegro_api.models.category_parameter_options import CategoryParameterOptions
from allegro_api.models.cells import Cells
from allegro_api.models.change_price import ChangePrice
from allegro_api.models.change_price_input import ChangePriceInput
from allegro_api.models.change_price_without_output import ChangePriceWithoutOutput
from allegro_api.models.checkout_form import CheckoutForm
from allegro_api.models.checkout_form_add_waybill_created import CheckoutFormAddWaybillCreated
from allegro_api.models.checkout_form_add_waybill_request import CheckoutFormAddWaybillRequest
from allegro_api.models.checkout_form_additional_service import CheckoutFormAdditionalService
from allegro_api.models.checkout_form_buyer_reference import CheckoutFormBuyerReference
from allegro_api.models.checkout_form_delivery_address import CheckoutFormDeliveryAddress
from allegro_api.models.checkout_form_delivery_method import CheckoutFormDeliveryMethod
from allegro_api.models.checkout_form_delivery_pickup_point import CheckoutFormDeliveryPickupPoint
from allegro_api.models.checkout_form_delivery_pickup_point_address import CheckoutFormDeliveryPickupPointAddress
from allegro_api.models.checkout_form_delivery_reference import CheckoutFormDeliveryReference
from allegro_api.models.checkout_form_discount import CheckoutFormDiscount
from allegro_api.models.checkout_form_invoice_address import CheckoutFormInvoiceAddress
from allegro_api.models.checkout_form_invoice_address_company import CheckoutFormInvoiceAddressCompany
from allegro_api.models.checkout_form_invoice_address_natural_person import CheckoutFormInvoiceAddressNaturalPerson
from allegro_api.models.checkout_form_invoice_info import CheckoutFormInvoiceInfo
from allegro_api.models.checkout_form_line_item import CheckoutFormLineItem
from allegro_api.models.checkout_form_order_waybill_response import CheckoutFormOrderWaybillResponse
from allegro_api.models.checkout_form_payment_provider import CheckoutFormPaymentProvider
from allegro_api.models.checkout_form_payment_reference import CheckoutFormPaymentReference
from allegro_api.models.checkout_form_payment_type import CheckoutFormPaymentType
from allegro_api.models.checkout_form_reference import CheckoutFormReference
from allegro_api.models.checkout_form_status import CheckoutFormStatus
from allegro_api.models.checkout_form_summary import CheckoutFormSummary
from allegro_api.models.checkout_forms import CheckoutForms
from allegro_api.models.command_output import CommandOutput
from allegro_api.models.command_task import CommandTask
from allegro_api.models.compatibility_list import CompatibilityList
from allegro_api.models.compatibility_list_item import CompatibilityListItem
from allegro_api.models.configuration import Configuration
from allegro_api.models.constraint_criteria import ConstraintCriteria
from allegro_api.models.contact_request import ContactRequest
from allegro_api.models.contact_response import ContactResponse
from allegro_api.models.contact_response_list import ContactResponseList
from allegro_api.models.coordinates import Coordinates
from allegro_api.models.definitions_response import DefinitionsResponse
from allegro_api.models.delivery import Delivery
from allegro_api.models.describes_listing_fee import DescribesListingFee
from allegro_api.models.describes_success_commission_fee import DescribesSuccessCommissionFee
from allegro_api.models.description_section import DescriptionSection
from allegro_api.models.description_section_item import DescriptionSectionItem
from allegro_api.models.description_section_item_image import DescriptionSectionItemImage
from allegro_api.models.description_section_item_text import DescriptionSectionItemText
from allegro_api.models.dictionary_category_parameter import DictionaryCategoryParameter
from allegro_api.models.dispute import Dispute
from allegro_api.models.dispute_attachment import DisputeAttachment
from allegro_api.models.dispute_attachment_id import DisputeAttachmentId
from allegro_api.models.dispute_author import DisputeAuthor
from allegro_api.models.dispute_author_role import DisputeAuthorRole
from allegro_api.models.dispute_checkout_form import DisputeCheckoutForm
from allegro_api.models.dispute_first_message import DisputeFirstMessage
from allegro_api.models.dispute_list_response import DisputeListResponse
from allegro_api.models.dispute_message import DisputeMessage
from allegro_api.models.dispute_message_author import DisputeMessageAuthor
from allegro_api.models.dispute_message_list import DisputeMessageList
from allegro_api.models.dispute_user import DisputeUser
from allegro_api.models.email_request import EmailRequest
from allegro_api.models.email_response import EmailResponse
from allegro_api.models.error import Error
from allegro_api.models.errors_holder import ErrorsHolder
from allegro_api.models.fee import Fee
from allegro_api.models.float_category_parameter import FloatCategoryParameter
from allegro_api.models.full_definition_response import FullDefinitionResponse
from allegro_api.models.general_report import GeneralReport
from allegro_api.models.get_sale_products_response import GetSaleProductsResponse
from allegro_api.models.header import Header
from allegro_api.models.image_url import ImageUrl
from allegro_api.models.implied_warranties_list_implied_warranty_basic import ImpliedWarrantiesListImpliedWarrantyBasic
from allegro_api.models.implied_warranty_basic import ImpliedWarrantyBasic
from allegro_api.models.inline_response200 import InlineResponse200
from allegro_api.models.inline_response2001 import InlineResponse2001
from allegro_api.models.inline_response2001_delivery_methods import InlineResponse2001DeliveryMethods
from allegro_api.models.inline_response200_shipping_rates import InlineResponse200ShippingRates
from allegro_api.models.integer_category_parameter import IntegerCategoryParameter
from allegro_api.models.just_id import JustId
from allegro_api.models.latest_order_event import LatestOrderEvent
from allegro_api.models.line_item_id_mappings import LineItemIdMappings
from allegro_api.models.line_item_id_mappings_mappings import LineItemIdMappingsMappings
from allegro_api.models.listing_category import ListingCategory
from allegro_api.models.listing_offer import ListingOffer
from allegro_api.models.listing_response import ListingResponse
from allegro_api.models.listing_response_categories import ListingResponseCategories
from allegro_api.models.listing_response_filters import ListingResponseFilters
from allegro_api.models.listing_response_filters_values import ListingResponseFiltersValues
from allegro_api.models.listing_response_offers import ListingResponseOffers
from allegro_api.models.listing_response_search_meta import ListingResponseSearchMeta
from allegro_api.models.listing_response_sort import ListingResponseSort
from allegro_api.models.location import Location
from allegro_api.models.message_author_role import MessageAuthorRole
from allegro_api.models.message_request import MessageRequest
from allegro_api.models.modification import Modification
from allegro_api.models.modification_delivery import ModificationDelivery
from allegro_api.models.modification_payments import ModificationPayments
from allegro_api.models.modification_promotion import ModificationPromotion
from allegro_api.models.modification_size_table import ModificationSizeTable
from allegro_api.models.monetary_amount import MonetaryAmount
from allegro_api.models.offer import Offer
from allegro_api.models.offer_attachment import OfferAttachment
from allegro_api.models.offer_attachment_request import OfferAttachmentRequest
from allegro_api.models.offer_category import OfferCategory
from allegro_api.models.offer_change_command import OfferChangeCommand
from allegro_api.models.offer_criterion import OfferCriterion
from allegro_api.models.offer_criterium import OfferCriterium
from allegro_api.models.offer_delivery import OfferDelivery
from allegro_api.models.offer_description import OfferDescription
from allegro_api.models.offer_fixed_price import OfferFixedPrice
from allegro_api.models.offer_id import OfferId
from allegro_api.models.offer_images import OfferImages
from allegro_api.models.offer_listing_dto_v1 import OfferListingDtoV1
from allegro_api.models.offer_listing_dto_v1_category import OfferListingDtoV1Category
from allegro_api.models.offer_listing_dto_v1_image import OfferListingDtoV1Image
from allegro_api.models.offer_listing_dto_v1_offer_status import OfferListingDtoV1OfferStatus
from allegro_api.models.offer_listing_dto_v1_offer_type import OfferListingDtoV1OfferType
from allegro_api.models.offer_listing_dto_v1_publication import OfferListingDtoV1Publication
from allegro_api.models.offer_listing_dto_v1_sale_info import OfferListingDtoV1SaleInfo
from allegro_api.models.offer_listing_dto_v1_selling_mode import OfferListingDtoV1SellingMode
from allegro_api.models.offer_listing_dto_v1_stats import OfferListingDtoV1Stats
from allegro_api.models.offer_listing_dto_v1_stock import OfferListingDtoV1Stock
from allegro_api.models.offer_lowest_price import OfferLowestPrice
from allegro_api.models.offer_price import OfferPrice
from allegro_api.models.offer_price_change_command import OfferPriceChangeCommand
from allegro_api.models.offer_promotion import OfferPromotion
from allegro_api.models.offer_publication import OfferPublication
from allegro_api.models.offer_quantity_change_command import OfferQuantityChangeCommand
from allegro_api.models.offer_quote_dto import OfferQuoteDto
from allegro_api.models.offer_quotes_dto import OfferQuotesDto
from allegro_api.models.offer_reference import OfferReference
from allegro_api.models.offer_seller import OfferSeller
from allegro_api.models.offer_selling_mode import OfferSellingMode
from allegro_api.models.offer_stock import OfferStock
from allegro_api.models.offer_vendor import OfferVendor
from allegro_api.models.offers_search_result_dto_v1 import OffersSearchResultDtoV1
from allegro_api.models.open_hour import OpenHour
from allegro_api.models.order import Order
from allegro_api.models.order_event import OrderEvent
from allegro_api.models.order_event_data import OrderEventData
from allegro_api.models.order_event_stats import OrderEventStats
from allegro_api.models.order_events_list import OrderEventsList
from allegro_api.models.order_line_item import OrderLineItem
from allegro_api.models.parameter import Parameter
from allegro_api.models.parameter_range_value import ParameterRangeValue
from allegro_api.models.parameters_for_preview_price import ParametersForPreviewPrice
from allegro_api.models.payment import Payment
from allegro_api.models.payments import Payments
from allegro_api.models.phones_request import PhonesRequest
from allegro_api.models.phones_response import PhonesResponse
from allegro_api.models.pos import Pos
from allegro_api.models.price import Price
from allegro_api.models.price_modification import PriceModification
from allegro_api.models.price_modification_fixed_price import PriceModificationFixedPrice
from allegro_api.models.price_modification_value_change import PriceModificationValueChange
from allegro_api.models.processing_status import ProcessingStatus
from allegro_api.models.product_parameter import ProductParameter
from allegro_api.models.product_parameter_options import ProductParameterOptions
from allegro_api.models.promotion import Promotion
from allegro_api.models.promotion_campaign_request_dto import PromotionCampaignRequestDto
from allegro_api.models.promotion_campaign_response_dto import PromotionCampaignResponseDto
from allegro_api.models.promotion_campaigns_response_dto import PromotionCampaignsResponseDto
from allegro_api.models.promotion_request_dto import PromotionRequestDto
from allegro_api.models.promotion_response_dto import PromotionResponseDto
from allegro_api.models.public_table_dto import PublicTableDto
from allegro_api.models.public_table_image_dto import PublicTableImageDto
from allegro_api.models.public_tables_dto import PublicTablesDto
from allegro_api.models.publication import Publication
from allegro_api.models.publication_change_command_dto import PublicationChangeCommandDto
from allegro_api.models.publication_modification import PublicationModification
from allegro_api.models.quantity_modification import QuantityModification
from allegro_api.models.rates import Rates
from allegro_api.models.reference import Reference
from allegro_api.models.removal import Removal
from allegro_api.models.removal_request import RemovalRequest
from allegro_api.models.return_policies_list_return_policy_basic import ReturnPoliciesListReturnPolicyBasic
from allegro_api.models.return_policy_basic import ReturnPolicyBasic
from allegro_api.models.sale_product_response_dto import SaleProductResponseDto
from allegro_api.models.search_result import SearchResult
from allegro_api.models.seller import Seller
from allegro_api.models.seller_create_rebate_request_dto import SellerCreateRebateRequestDto
from allegro_api.models.seller_rebate_dto import SellerRebateDto
from allegro_api.models.seller_rebates_dto import SellerRebatesDto
from allegro_api.models.seller_reference import SellerReference
from allegro_api.models.selling_mode import SellingMode
from allegro_api.models.shipping_rates import ShippingRates
from allegro_api.models.shipping_rates_set import ShippingRatesSet
from allegro_api.models.shipping_rates_set_rates import ShippingRatesSetRates
from allegro_api.models.shipping_rates_set_rates_delivery_method import ShippingRatesSetRatesDeliveryMethod
from allegro_api.models.shipping_rates_set_rates_first_item_rate import ShippingRatesSetRatesFirstItemRate
from allegro_api.models.shipping_rates_set_rates_next_item_rate import ShippingRatesSetRatesNextItemRate
from allegro_api.models.shipping_rates_set_rates_shipping_time import ShippingRatesSetRatesShippingTime
from allegro_api.models.single_promotion_campaign_response_dto import SinglePromotionCampaignResponseDto
from allegro_api.models.stock import Stock
from allegro_api.models.string_category_parameter import StringCategoryParameter
from allegro_api.models.subject import Subject
from allegro_api.models.summary import Summary
from allegro_api.models.tag_id import TagId
from allegro_api.models.tag_ids_request import TagIdsRequest
from allegro_api.models.tag_list_response import TagListResponse
from allegro_api.models.tag_request import TagRequest
from allegro_api.models.tag_response import TagResponse
from allegro_api.models.task_count import TaskCount
from allegro_api.models.task_report import TaskReport
from allegro_api.models.user import User
from allegro_api.models.user_rating import UserRating
from allegro_api.models.user_rating_list_response import UserRatingListResponse
from allegro_api.models.user_rating_summary_response import UserRatingSummaryResponse
from allegro_api.models.validation import Validation
from allegro_api.models.validation_error import ValidationError
from allegro_api.models.variant_set import VariantSet
from allegro_api.models.variant_set_offer import VariantSetOffer
from allegro_api.models.variant_set_parameter import VariantSetParameter
from allegro_api.models.variant_sets import VariantSets
from allegro_api.models.variant_sets_variant_set import VariantSetsVariantSet
from allegro_api.models.warranties_list_warranty_basic import WarrantiesListWarrantyBasic
from allegro_api.models.warranty_basic import WarrantyBasic
from allegro_api.models.wrapper_type_for_preview_conditions import WrapperTypeForPreviewConditions
from allegro_api.models.wraps_listing_and_commissions_fees import WrapsListingAndCommissionsFees
