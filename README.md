# allegro-pl-rest-api
https://developer.allegro.pl/about

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: latest
- Package version: 2019.2
- Build date: 2019-04-02T00:25:32.785731+02:00[Europe/Warsaw]
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import allegro_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import allegro_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.AdditionalServicesApi(allegro_api.ApiClient(configuration))
additional_services_group_request = allegro_api.AdditionalServicesGroupRequest() # AdditionalServicesGroupRequest | Additional service group body

try:
    # Create additional services group
    api_response = api_instance.create_additional_services_group_using_post(additional_services_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->create_additional_services_group_using_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.allegro.pl*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdditionalServicesApi* | [**create_additional_services_group_using_post**](docs/AdditionalServicesApi.md#create_additional_services_group_using_post) | **POST** /sale/offer-additional-services/groups | Create additional services group
*AdditionalServicesApi* | [**get_additional_services_group_using_get**](docs/AdditionalServicesApi.md#get_additional_services_group_using_get) | **GET** /sale/offer-additional-services/groups/{groupId} | Get the details of an additional services group
*AdditionalServicesApi* | [**get_list_of_additional_services_definitions_using_get**](docs/AdditionalServicesApi.md#get_list_of_additional_services_definitions_using_get) | **GET** /sale/offer-additional-services/definitions | Get the user&#39;s additional services definitions
*AdditionalServicesApi* | [**get_list_of_additional_services_groups_using_get**](docs/AdditionalServicesApi.md#get_list_of_additional_services_groups_using_get) | **GET** /sale/offer-additional-services/groups | Get the user&#39;s additional services groups
*AdditionalServicesApi* | [**modify_additional_services_group_using_put**](docs/AdditionalServicesApi.md#modify_additional_services_group_using_put) | **PUT** /sale/offer-additional-services/groups/{groupId} | Modify an additional services group
*AfterSaleServicesApi* | [**get_public_seller_listing_using_get**](docs/AfterSaleServicesApi.md#get_public_seller_listing_using_get) | **GET** /after-sales-service-conditions/implied-warranties | Get the user&#39;s implied warranties
*AfterSaleServicesApi* | [**get_public_seller_listing_using_get1**](docs/AfterSaleServicesApi.md#get_public_seller_listing_using_get1) | **GET** /after-sales-service-conditions/return-policies | Get the user&#39;s return policies
*AfterSaleServicesApi* | [**get_public_seller_listing_using_get2**](docs/AfterSaleServicesApi.md#get_public_seller_listing_using_get2) | **GET** /after-sales-service-conditions/warranties | Get the user&#39;s warranties
*BatchOfferModificationApi* | [**get_general_report_using_get**](docs/BatchOfferModificationApi.md#get_general_report_using_get) | **GET** /sale/offer-modification-commands/{commandId} | Modification command summary
*BatchOfferModificationApi* | [**get_price_modification_command_status_using_get**](docs/BatchOfferModificationApi.md#get_price_modification_command_status_using_get) | **GET** /sale/offer-price-change-commands/{commandId} | Change price command summary
*BatchOfferModificationApi* | [**get_price_modification_command_tasks_statuses_using_get**](docs/BatchOfferModificationApi.md#get_price_modification_command_tasks_statuses_using_get) | **GET** /sale/offer-price-change-commands/{commandId}/tasks | Change price command detailed report
*BatchOfferModificationApi* | [**get_quantity_modification_command_status_using_get**](docs/BatchOfferModificationApi.md#get_quantity_modification_command_status_using_get) | **GET** /sale/offer-quantity-change-commands/{commandId} | Change quantity command summary
*BatchOfferModificationApi* | [**get_quantity_modification_command_tasks_statuses_using_get**](docs/BatchOfferModificationApi.md#get_quantity_modification_command_tasks_statuses_using_get) | **GET** /sale/offer-quantity-change-commands/{commandId}/tasks | Change quantity command detailed report
*BatchOfferModificationApi* | [**get_tasks_using_get**](docs/BatchOfferModificationApi.md#get_tasks_using_get) | **GET** /sale/offer-modification-commands/{commandId}/tasks | Modification command detailed report
*BatchOfferModificationApi* | [**modification_command_using_put**](docs/BatchOfferModificationApi.md#modification_command_using_put) | **PUT** /sale/offer-modification-commands/{commandId} | Batch offer modification
*BatchOfferModificationApi* | [**price_modification_command_using_put**](docs/BatchOfferModificationApi.md#price_modification_command_using_put) | **PUT** /sale/offer-price-change-commands/{commandId} | Batch offer price modification
*BatchOfferModificationApi* | [**quantity_modification_command_using_put**](docs/BatchOfferModificationApi.md#quantity_modification_command_using_put) | **PUT** /sale/offer-quantity-change-commands/{commandId} | Batch offer quantity modification
*CategoriesAndParametersApi* | [**get_categories_using_get**](docs/CategoriesAndParametersApi.md#get_categories_using_get) | **GET** /sale/categories | Get IDs of main Allegro categories
*CategoriesAndParametersApi* | [**get_category_using_get1**](docs/CategoriesAndParametersApi.md#get_category_using_get1) | **GET** /sale/categories/{categoryId} | Get category by ID
*CategoriesAndParametersApi* | [**get_flat_parameters_using_get2**](docs/CategoriesAndParametersApi.md#get_flat_parameters_using_get2) | **GET** /sale/categories/{categoryId}/parameters | Get parameters by category ID
*ContactsApi* | [**create_contact_using_post**](docs/ContactsApi.md#create_contact_using_post) | **POST** /sale/offer-contacts | Create a new contact
*ContactsApi* | [**get_contact_using_get**](docs/ContactsApi.md#get_contact_using_get) | **GET** /sale/offer-contacts/{id} | Get contact details
*ContactsApi* | [**get_list_of_contacts_using_get**](docs/ContactsApi.md#get_list_of_contacts_using_get) | **GET** /sale/offer-contacts | Get the user&#39;s contacts
*ContactsApi* | [**modify_contact_using_put**](docs/ContactsApi.md#modify_contact_using_put) | **PUT** /sale/offer-contacts/{id} | Modify contact details
*DeliveryApi* | [**create_shipping_rates_set_using_post**](docs/DeliveryApi.md#create_shipping_rates_set_using_post) | **POST** /sale/shipping-rates | Create a new shipping rates set
*DeliveryApi* | [**get_list_of_delivery_methods_using_get**](docs/DeliveryApi.md#get_list_of_delivery_methods_using_get) | **GET** /sale/delivery-methods | Get the list of available delivery methods
*DeliveryApi* | [**get_list_of_shipping_ratest_using_get**](docs/DeliveryApi.md#get_list_of_shipping_ratest_using_get) | **GET** /sale/shipping-rates | Get the user&#39;s shipping rates
*DeliveryApi* | [**get_shipping_rates_set_using_get**](docs/DeliveryApi.md#get_shipping_rates_set_using_get) | **GET** /sale/shipping-rates/{id} | Get the details of a shipping rates set
*DeliveryApi* | [**modify_shipiing_rates_set_using_put**](docs/DeliveryApi.md#modify_shipiing_rates_set_using_put) | **PUT** /sale/shipping-rates/{id} | Edit a user&#39;s shipping rates set
*DisputesApi* | [**add_message_to_dispute_using_post**](docs/DisputesApi.md#add_message_to_dispute_using_post) | **POST** /sale/disputes/{disputeId}/messages | Add a message to a dispute
*DisputesApi* | [**create_an_attachment_using_post**](docs/DisputesApi.md#create_an_attachment_using_post) | **POST** /sale/dispute-attachments | Create an attachment declaration
*DisputesApi* | [**get_attachment_using_get**](docs/DisputesApi.md#get_attachment_using_get) | **GET** /sale/dispute-attachments/{attachmentId} | Get an attachment
*DisputesApi* | [**get_dispute_using_get**](docs/DisputesApi.md#get_dispute_using_get) | **GET** /sale/disputes/{disputeId} | Get a single dispute
*DisputesApi* | [**get_list_of_disputes_using_get**](docs/DisputesApi.md#get_list_of_disputes_using_get) | **GET** /sale/disputes | Get the user&#39;s disputes
*DisputesApi* | [**get_messages_from_dispute_using_get**](docs/DisputesApi.md#get_messages_from_dispute_using_get) | **GET** /sale/disputes/{disputeId}/messages | Get the messages within a dispute
*ImagesAndAttachmentsApi* | [**create_offer_attachment_using_post**](docs/ImagesAndAttachmentsApi.md#create_offer_attachment_using_post) | **POST** /sale/offer-attachments | Create an offer attachment
*ListingBadgesApi* | [**add_promotion_to_campaign_using_post**](docs/ListingBadgesApi.md#add_promotion_to_campaign_using_post) | **POST** /sale/loyalty/promotion-campaigns | Create an application for a promotion campaign
*ListingBadgesApi* | [**delete_campaign_from_promotion_using_delete**](docs/ListingBadgesApi.md#delete_campaign_from_promotion_using_delete) | **DELETE** /sale/loyalty/promotion-campaigns | Delete a campaign in a promotion
*ListingBadgesApi* | [**delete_promotion_campaign_application_using_delete**](docs/ListingBadgesApi.md#delete_promotion_campaign_application_using_delete) | **DELETE** /sale/loyalty/promotion-campaign-applications/{applicationId} | Delete an application for promotion campaign
*ListingBadgesApi* | [**get_promotion_campaign_application_using_get**](docs/ListingBadgesApi.md#get_promotion_campaign_application_using_get) | **GET** /sale/loyalty/promotion-campaign-applications/{applicationId} | Get an application for promotion campaign
*ListingBadgesApi* | [**get_promotion_campaigns_using_get**](docs/ListingBadgesApi.md#get_promotion_campaigns_using_get) | **GET** /sale/loyalty/promotion-campaigns | Get the user&#39;s promotion campaigns
*OfferManagementApi* | [**change_publication_status_using_put**](docs/OfferManagementApi.md#change_publication_status_using_put) | **PUT** /sale/offer-publication-commands/{commandId} | Batch offer publish / unpublish
*OfferManagementApi* | [**create_change_price_command_using_put**](docs/OfferManagementApi.md#create_change_price_command_using_put) | **PUT** /offers/{offerId}/change-price-commands/{commandId} | Modify the Buy Now price in an offer
*OfferManagementApi* | [**create_offer_using_post**](docs/OfferManagementApi.md#create_offer_using_post) | **POST** /sale/offers | Create a draft offer
*OfferManagementApi* | [**delete_offer_using_delete**](docs/OfferManagementApi.md#delete_offer_using_delete) | **DELETE** /sale/offers/{offerId} | Delete a draft offer
*OfferManagementApi* | [**get_publication_report_using_get**](docs/OfferManagementApi.md#get_publication_report_using_get) | **GET** /sale/offer-publication-commands/{commandId} | Publish command summary
*OfferManagementApi* | [**get_publication_tasks_using_get**](docs/OfferManagementApi.md#get_publication_tasks_using_get) | **GET** /sale/offer-publication-commands/{commandId}/tasks | Publish command detailed report
*OfferManagementApi* | [**update_offer_using_put**](docs/OfferManagementApi.md#update_offer_using_put) | **PUT** /sale/offers/{offerId} | Complete a draft offer or edit an offer
*OfferTagsApi* | [**assign_tag_to_offer_post**](docs/OfferTagsApi.md#assign_tag_to_offer_post) | **POST** /sale/offers/{offerId}/tags | Assign tags to an offer
*OfferTagsApi* | [**create_tag_post1**](docs/OfferTagsApi.md#create_tag_post1) | **POST** /sale/offer-tags | Create a tag
*OfferTagsApi* | [**delete_tag_using_delete**](docs/OfferTagsApi.md#delete_tag_using_delete) | **DELETE** /sale/offer-tags/{tagId} | Delete a tag
*OfferTagsApi* | [**list_assigned_offer_tags_get**](docs/OfferTagsApi.md#list_assigned_offer_tags_get) | **GET** /sale/offers/{offerId}/tags | Get tags assigned to an offer
*OfferTagsApi* | [**list_seller_tags_get1**](docs/OfferTagsApi.md#list_seller_tags_get1) | **GET** /sale/offer-tags | Get the user&#39;s tags
*OfferTagsApi* | [**update_tag_put**](docs/OfferTagsApi.md#update_tag_put) | **PUT** /sale/offer-tags/{tagId} | Modify a tag
*OfferVariantsApi* | [**create_or_update_variant_set**](docs/OfferVariantsApi.md#create_or_update_variant_set) | **PUT** /sale/offer-variants/{setId} | [BETA] Create or update variant set
*OfferVariantsApi* | [**delete_variant_set**](docs/OfferVariantsApi.md#delete_variant_set) | **DELETE** /sale/offer-variants/{setId} | [BETA] Delete a variant set
*OfferVariantsApi* | [**get_variant_set**](docs/OfferVariantsApi.md#get_variant_set) | **GET** /sale/offer-variants/{setId} | [BETA] Get a variant set
*OfferVariantsApi* | [**get_variant_sets**](docs/OfferVariantsApi.md#get_variant_sets) | **GET** /sale/offer-variants | [BETA] Get the user&#39;s variant sets
*OrderManagementApi* | [**create_order_shipments_using_post**](docs/OrderManagementApi.md#create_order_shipments_using_post) | **POST** /order/checkout-forms/{id}/shipments | [BETA] Add a parcel tracking number
*OrderManagementApi* | [**find_mapping**](docs/OrderManagementApi.md#find_mapping) | **GET** /order/line-item-id-mappings | [BETA] Get mapping for line item id
*OrderManagementApi* | [**get_list_of_orders_using_get**](docs/OrderManagementApi.md#get_list_of_orders_using_get) | **GET** /order/checkout-forms | [BETA] Get the user&#39;s orders
*OrderManagementApi* | [**get_order_events_statistics_using_get**](docs/OrderManagementApi.md#get_order_events_statistics_using_get) | **GET** /order/event-stats | [BETA] Get order events statistics
*OrderManagementApi* | [**get_order_events_using_get**](docs/OrderManagementApi.md#get_order_events_using_get) | **GET** /order/events | [BETA] Get order events
*OrderManagementApi* | [**get_order_shipments_using_get**](docs/OrderManagementApi.md#get_order_shipments_using_get) | **GET** /order/checkout-forms/{id}/shipments | [BETA] Get a list of parcel tracking numbers
*OrderManagementApi* | [**get_orders_details_using_get**](docs/OrderManagementApi.md#get_orders_details_using_get) | **GET** /order/checkout-forms/{id} | [BETA] Get an order&#39;s details
*PointsOfServiceApi* | [**create_pos_using_post**](docs/PointsOfServiceApi.md#create_pos_using_post) | **POST** /points-of-service | Create a point of service
*PointsOfServiceApi* | [**delete_pos_using_delete**](docs/PointsOfServiceApi.md#delete_pos_using_delete) | **DELETE** /points-of-service/{id} | Delete a point of service
*PointsOfServiceApi* | [**get_pos_data_using_get**](docs/PointsOfServiceApi.md#get_pos_data_using_get) | **GET** /points-of-service/{id} | Get the details of a point of service
*PointsOfServiceApi* | [**get_pos_list_using_get**](docs/PointsOfServiceApi.md#get_pos_list_using_get) | **GET** /points-of-service | Get the user&#39;s points of service
*PointsOfServiceApi* | [**modify_pos_using_put**](docs/PointsOfServiceApi.md#modify_pos_using_put) | **PUT** /points-of-service/{id} | Modify a point of service
*PricingApi* | [**offer_quotes_public_using_get**](docs/PricingApi.md#offer_quotes_public_using_get) | **GET** /pricing/offer-quotes | Get the user&#39;s current offer quotes
*PricingApi* | [**preview_fees_public_api_using_post**](docs/PricingApi.md#preview_fees_public_api_using_post) | **POST** /pricing/fee-preview | Preview offer fees
*ProductsApi* | [**get_sale_product**](docs/ProductsApi.md#get_sale_product) | **GET** /sale/products/{productId} | Get all data of the particular product
*ProductsApi* | [**get_sale_products**](docs/ProductsApi.md#get_sale_products) | **GET** /sale/products | Get search products results
*PublicOfferInformationApi* | [**get_listing**](docs/PublicOfferInformationApi.md#get_listing) | **GET** /offers/listing | Search offers
*PublicUserInformationApi* | [**get_user_summary_using_get**](docs/PublicUserInformationApi.md#get_user_summary_using_get) | **GET** /users/{userId}/ratings-summary | Get any user&#39;s ratings summary
*SetsAndRebatesApi* | [**create_promotion_using_post1**](docs/SetsAndRebatesApi.md#create_promotion_using_post1) | **POST** /sale/loyalty/promotions | Create a new promotion
*SetsAndRebatesApi* | [**deactivate_promotion_using_delete**](docs/SetsAndRebatesApi.md#deactivate_promotion_using_delete) | **DELETE** /sale/loyalty/promotions/{promotionId} | Deactivate a promotion by id
*SetsAndRebatesApi* | [**get_promotion_using_get**](docs/SetsAndRebatesApi.md#get_promotion_using_get) | **GET** /sale/loyalty/promotions/{promotionId} | Get a promotion data by id
*SetsAndRebatesApi* | [**list_seller_promotions_using_get1**](docs/SetsAndRebatesApi.md#list_seller_promotions_using_get1) | **GET** /sale/loyalty/promotions | Get the user&#39;s list of promotions
*SizeTablesApi* | [**get_table_using_get**](docs/SizeTablesApi.md#get_table_using_get) | **GET** /sale/size-tables/{tableId} | Get a size table details
*SizeTablesApi* | [**get_tables_using_get**](docs/SizeTablesApi.md#get_tables_using_get) | **GET** /sale/size-tables | Get the user&#39;s size tables
*UserInformationApi* | [**get_user_ratings_using_get**](docs/UserInformationApi.md#get_user_ratings_using_get) | **GET** /sale/user-ratings | Get the user&#39;s ratings
*UsersOfferInformationApi* | [**get_offer_using_get**](docs/UsersOfferInformationApi.md#get_offer_using_get) | **GET** /sale/offers/{offerId} | Get all fields of the particular offer
*UsersOfferInformationApi* | [**search_offers_using_get**](docs/UsersOfferInformationApi.md#search_offers_using_get) | **GET** /sale/offers | Get seller&#39;s offers


## Documentation For Models

 - [AdditionalServiceDefinitionRequest](docs/AdditionalServiceDefinitionRequest.md)
 - [AdditionalServiceRequest](docs/AdditionalServiceRequest.md)
 - [AdditionalServiceResponse](docs/AdditionalServiceResponse.md)
 - [AdditionalServicesGroup](docs/AdditionalServicesGroup.md)
 - [AdditionalServicesGroupRequest](docs/AdditionalServicesGroupRequest.md)
 - [AdditionalServicesGroupResponse](docs/AdditionalServicesGroupResponse.md)
 - [AdditionalServicesGroups](docs/AdditionalServicesGroups.md)
 - [Address](docs/Address.md)
 - [AfterSalesServices](docs/AfterSalesServices.md)
 - [Answer](docs/Answer.md)
 - [AttachmentDeclaration](docs/AttachmentDeclaration.md)
 - [AttachmentFile](docs/AttachmentFile.md)
 - [AttachmentFileRequest](docs/AttachmentFileRequest.md)
 - [AttachmentType](docs/AttachmentType.md)
 - [AvailableConstraint](docs/AvailableConstraint.md)
 - [AverageRates](docs/AverageRates.md)
 - [BasicDefinitionResponse](docs/BasicDefinitionResponse.md)
 - [Benefit](docs/Benefit.md)
 - [BenefitSpecification](docs/BenefitSpecification.md)
 - [BuyerReference](docs/BuyerReference.md)
 - [CampaignRequestDto](docs/CampaignRequestDto.md)
 - [CampaignResponseDto](docs/CampaignResponseDto.md)
 - [Caption](docs/Caption.md)
 - [CategoriesDto](docs/CategoriesDto.md)
 - [Category](docs/Category.md)
 - [CategoryDto](docs/CategoryDto.md)
 - [CategoryIdDto](docs/CategoryIdDto.md)
 - [CategoryOptionsDto](docs/CategoryOptionsDto.md)
 - [CategoryParameter](docs/CategoryParameter.md)
 - [CategoryParameterList](docs/CategoryParameterList.md)
 - [CategoryParameterOptions](docs/CategoryParameterOptions.md)
 - [Cells](docs/Cells.md)
 - [ChangePrice](docs/ChangePrice.md)
 - [ChangePriceInput](docs/ChangePriceInput.md)
 - [ChangePriceWithoutOutput](docs/ChangePriceWithoutOutput.md)
 - [CheckoutForm](docs/CheckoutForm.md)
 - [CheckoutFormAddWaybillCreated](docs/CheckoutFormAddWaybillCreated.md)
 - [CheckoutFormAddWaybillRequest](docs/CheckoutFormAddWaybillRequest.md)
 - [CheckoutFormAdditionalService](docs/CheckoutFormAdditionalService.md)
 - [CheckoutFormBuyerReference](docs/CheckoutFormBuyerReference.md)
 - [CheckoutFormDeliveryAddress](docs/CheckoutFormDeliveryAddress.md)
 - [CheckoutFormDeliveryMethod](docs/CheckoutFormDeliveryMethod.md)
 - [CheckoutFormDeliveryPickupPoint](docs/CheckoutFormDeliveryPickupPoint.md)
 - [CheckoutFormDeliveryPickupPointAddress](docs/CheckoutFormDeliveryPickupPointAddress.md)
 - [CheckoutFormDeliveryReference](docs/CheckoutFormDeliveryReference.md)
 - [CheckoutFormDiscount](docs/CheckoutFormDiscount.md)
 - [CheckoutFormInvoiceAddress](docs/CheckoutFormInvoiceAddress.md)
 - [CheckoutFormInvoiceAddressCompany](docs/CheckoutFormInvoiceAddressCompany.md)
 - [CheckoutFormInvoiceAddressNaturalPerson](docs/CheckoutFormInvoiceAddressNaturalPerson.md)
 - [CheckoutFormInvoiceInfo](docs/CheckoutFormInvoiceInfo.md)
 - [CheckoutFormLineItem](docs/CheckoutFormLineItem.md)
 - [CheckoutFormOrderWaybillResponse](docs/CheckoutFormOrderWaybillResponse.md)
 - [CheckoutFormPaymentProvider](docs/CheckoutFormPaymentProvider.md)
 - [CheckoutFormPaymentReference](docs/CheckoutFormPaymentReference.md)
 - [CheckoutFormPaymentType](docs/CheckoutFormPaymentType.md)
 - [CheckoutFormReference](docs/CheckoutFormReference.md)
 - [CheckoutFormStatus](docs/CheckoutFormStatus.md)
 - [CheckoutFormSummary](docs/CheckoutFormSummary.md)
 - [CheckoutForms](docs/CheckoutForms.md)
 - [CommandOutput](docs/CommandOutput.md)
 - [CommandTask](docs/CommandTask.md)
 - [CompatibilityList](docs/CompatibilityList.md)
 - [CompatibilityListItem](docs/CompatibilityListItem.md)
 - [Configuration](docs/Configuration.md)
 - [ConstraintCriteria](docs/ConstraintCriteria.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [ContactResponse](docs/ContactResponse.md)
 - [ContactResponseList](docs/ContactResponseList.md)
 - [Coordinates](docs/Coordinates.md)
 - [DefinitionsResponse](docs/DefinitionsResponse.md)
 - [Delivery](docs/Delivery.md)
 - [DescribesListingFee](docs/DescribesListingFee.md)
 - [DescribesSuccessCommissionFee](docs/DescribesSuccessCommissionFee.md)
 - [DescriptionSection](docs/DescriptionSection.md)
 - [DescriptionSectionItem](docs/DescriptionSectionItem.md)
 - [DescriptionSectionItemImage](docs/DescriptionSectionItemImage.md)
 - [DescriptionSectionItemText](docs/DescriptionSectionItemText.md)
 - [DictionaryCategoryParameter](docs/DictionaryCategoryParameter.md)
 - [Dispute](docs/Dispute.md)
 - [DisputeAttachment](docs/DisputeAttachment.md)
 - [DisputeAttachmentId](docs/DisputeAttachmentId.md)
 - [DisputeAuthor](docs/DisputeAuthor.md)
 - [DisputeAuthorRole](docs/DisputeAuthorRole.md)
 - [DisputeCheckoutForm](docs/DisputeCheckoutForm.md)
 - [DisputeFirstMessage](docs/DisputeFirstMessage.md)
 - [DisputeListResponse](docs/DisputeListResponse.md)
 - [DisputeMessage](docs/DisputeMessage.md)
 - [DisputeMessageAuthor](docs/DisputeMessageAuthor.md)
 - [DisputeMessageList](docs/DisputeMessageList.md)
 - [DisputeUser](docs/DisputeUser.md)
 - [EmailRequest](docs/EmailRequest.md)
 - [EmailResponse](docs/EmailResponse.md)
 - [Error](docs/Error.md)
 - [ErrorsHolder](docs/ErrorsHolder.md)
 - [Fee](docs/Fee.md)
 - [FloatCategoryParameter](docs/FloatCategoryParameter.md)
 - [FullDefinitionResponse](docs/FullDefinitionResponse.md)
 - [GeneralReport](docs/GeneralReport.md)
 - [GetSaleProductsResponse](docs/GetSaleProductsResponse.md)
 - [Header](docs/Header.md)
 - [ImageUrl](docs/ImageUrl.md)
 - [ImpliedWarrantiesListImpliedWarrantyBasic](docs/ImpliedWarrantiesListImpliedWarrantyBasic.md)
 - [ImpliedWarrantyBasic](docs/ImpliedWarrantyBasic.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001DeliveryMethods](docs/InlineResponse2001DeliveryMethods.md)
 - [InlineResponse200ShippingRates](docs/InlineResponse200ShippingRates.md)
 - [IntegerCategoryParameter](docs/IntegerCategoryParameter.md)
 - [JustId](docs/JustId.md)
 - [LatestOrderEvent](docs/LatestOrderEvent.md)
 - [LineItemIdMappings](docs/LineItemIdMappings.md)
 - [LineItemIdMappingsMappings](docs/LineItemIdMappingsMappings.md)
 - [ListingCategory](docs/ListingCategory.md)
 - [ListingOffer](docs/ListingOffer.md)
 - [ListingResponse](docs/ListingResponse.md)
 - [ListingResponseCategories](docs/ListingResponseCategories.md)
 - [ListingResponseFilters](docs/ListingResponseFilters.md)
 - [ListingResponseFiltersValues](docs/ListingResponseFiltersValues.md)
 - [ListingResponseOffers](docs/ListingResponseOffers.md)
 - [ListingResponseSearchMeta](docs/ListingResponseSearchMeta.md)
 - [ListingResponseSort](docs/ListingResponseSort.md)
 - [Location](docs/Location.md)
 - [MessageAuthorRole](docs/MessageAuthorRole.md)
 - [MessageRequest](docs/MessageRequest.md)
 - [Modification](docs/Modification.md)
 - [ModificationDelivery](docs/ModificationDelivery.md)
 - [ModificationPayments](docs/ModificationPayments.md)
 - [ModificationPromotion](docs/ModificationPromotion.md)
 - [ModificationSizeTable](docs/ModificationSizeTable.md)
 - [MonetaryAmount](docs/MonetaryAmount.md)
 - [Offer](docs/Offer.md)
 - [OfferAttachment](docs/OfferAttachment.md)
 - [OfferAttachmentRequest](docs/OfferAttachmentRequest.md)
 - [OfferCategory](docs/OfferCategory.md)
 - [OfferChangeCommand](docs/OfferChangeCommand.md)
 - [OfferCriterion](docs/OfferCriterion.md)
 - [OfferCriterium](docs/OfferCriterium.md)
 - [OfferDelivery](docs/OfferDelivery.md)
 - [OfferDescription](docs/OfferDescription.md)
 - [OfferFixedPrice](docs/OfferFixedPrice.md)
 - [OfferId](docs/OfferId.md)
 - [OfferImages](docs/OfferImages.md)
 - [OfferListingDtoV1](docs/OfferListingDtoV1.md)
 - [OfferListingDtoV1Category](docs/OfferListingDtoV1Category.md)
 - [OfferListingDtoV1Image](docs/OfferListingDtoV1Image.md)
 - [OfferListingDtoV1OfferStatus](docs/OfferListingDtoV1OfferStatus.md)
 - [OfferListingDtoV1OfferType](docs/OfferListingDtoV1OfferType.md)
 - [OfferListingDtoV1Publication](docs/OfferListingDtoV1Publication.md)
 - [OfferListingDtoV1SaleInfo](docs/OfferListingDtoV1SaleInfo.md)
 - [OfferListingDtoV1SellingMode](docs/OfferListingDtoV1SellingMode.md)
 - [OfferListingDtoV1Stats](docs/OfferListingDtoV1Stats.md)
 - [OfferListingDtoV1Stock](docs/OfferListingDtoV1Stock.md)
 - [OfferLowestPrice](docs/OfferLowestPrice.md)
 - [OfferPrice](docs/OfferPrice.md)
 - [OfferPriceChangeCommand](docs/OfferPriceChangeCommand.md)
 - [OfferPromotion](docs/OfferPromotion.md)
 - [OfferPublication](docs/OfferPublication.md)
 - [OfferQuantityChangeCommand](docs/OfferQuantityChangeCommand.md)
 - [OfferQuoteDto](docs/OfferQuoteDto.md)
 - [OfferQuotesDto](docs/OfferQuotesDto.md)
 - [OfferReference](docs/OfferReference.md)
 - [OfferSeller](docs/OfferSeller.md)
 - [OfferSellingMode](docs/OfferSellingMode.md)
 - [OfferStock](docs/OfferStock.md)
 - [OfferVendor](docs/OfferVendor.md)
 - [OffersSearchResultDtoV1](docs/OffersSearchResultDtoV1.md)
 - [OpenHour](docs/OpenHour.md)
 - [Order](docs/Order.md)
 - [OrderEvent](docs/OrderEvent.md)
 - [OrderEventData](docs/OrderEventData.md)
 - [OrderEventStats](docs/OrderEventStats.md)
 - [OrderEventsList](docs/OrderEventsList.md)
 - [OrderLineItem](docs/OrderLineItem.md)
 - [Parameter](docs/Parameter.md)
 - [ParameterRangeValue](docs/ParameterRangeValue.md)
 - [ParametersForPreviewPrice](docs/ParametersForPreviewPrice.md)
 - [Payment](docs/Payment.md)
 - [Payments](docs/Payments.md)
 - [PhonesRequest](docs/PhonesRequest.md)
 - [PhonesResponse](docs/PhonesResponse.md)
 - [Pos](docs/Pos.md)
 - [Price](docs/Price.md)
 - [PriceModification](docs/PriceModification.md)
 - [PriceModificationFixedPrice](docs/PriceModificationFixedPrice.md)
 - [PriceModificationValueChange](docs/PriceModificationValueChange.md)
 - [ProcessingStatus](docs/ProcessingStatus.md)
 - [ProductParameter](docs/ProductParameter.md)
 - [ProductParameterOptions](docs/ProductParameterOptions.md)
 - [Promotion](docs/Promotion.md)
 - [PromotionCampaignRequestDto](docs/PromotionCampaignRequestDto.md)
 - [PromotionCampaignResponseDto](docs/PromotionCampaignResponseDto.md)
 - [PromotionCampaignsResponseDto](docs/PromotionCampaignsResponseDto.md)
 - [PromotionRequestDto](docs/PromotionRequestDto.md)
 - [PromotionResponseDto](docs/PromotionResponseDto.md)
 - [PublicTableDto](docs/PublicTableDto.md)
 - [PublicTableImageDto](docs/PublicTableImageDto.md)
 - [PublicTablesDto](docs/PublicTablesDto.md)
 - [Publication](docs/Publication.md)
 - [PublicationChangeCommandDto](docs/PublicationChangeCommandDto.md)
 - [PublicationModification](docs/PublicationModification.md)
 - [QuantityModification](docs/QuantityModification.md)
 - [Rates](docs/Rates.md)
 - [Reference](docs/Reference.md)
 - [Removal](docs/Removal.md)
 - [RemovalRequest](docs/RemovalRequest.md)
 - [ReturnPoliciesListReturnPolicyBasic](docs/ReturnPoliciesListReturnPolicyBasic.md)
 - [ReturnPolicyBasic](docs/ReturnPolicyBasic.md)
 - [SaleProductResponseDto](docs/SaleProductResponseDto.md)
 - [SearchResult](docs/SearchResult.md)
 - [Seller](docs/Seller.md)
 - [SellerCreateRebateRequestDto](docs/SellerCreateRebateRequestDto.md)
 - [SellerRebateDto](docs/SellerRebateDto.md)
 - [SellerRebatesDto](docs/SellerRebatesDto.md)
 - [SellerReference](docs/SellerReference.md)
 - [SellingMode](docs/SellingMode.md)
 - [ShippingRates](docs/ShippingRates.md)
 - [ShippingRatesSet](docs/ShippingRatesSet.md)
 - [ShippingRatesSetRates](docs/ShippingRatesSetRates.md)
 - [ShippingRatesSetRatesDeliveryMethod](docs/ShippingRatesSetRatesDeliveryMethod.md)
 - [ShippingRatesSetRatesFirstItemRate](docs/ShippingRatesSetRatesFirstItemRate.md)
 - [ShippingRatesSetRatesNextItemRate](docs/ShippingRatesSetRatesNextItemRate.md)
 - [ShippingRatesSetRatesShippingTime](docs/ShippingRatesSetRatesShippingTime.md)
 - [SinglePromotionCampaignResponseDto](docs/SinglePromotionCampaignResponseDto.md)
 - [Stock](docs/Stock.md)
 - [StringCategoryParameter](docs/StringCategoryParameter.md)
 - [Subject](docs/Subject.md)
 - [Summary](docs/Summary.md)
 - [TagId](docs/TagId.md)
 - [TagIdsRequest](docs/TagIdsRequest.md)
 - [TagListResponse](docs/TagListResponse.md)
 - [TagRequest](docs/TagRequest.md)
 - [TagResponse](docs/TagResponse.md)
 - [TaskCount](docs/TaskCount.md)
 - [TaskReport](docs/TaskReport.md)
 - [User](docs/User.md)
 - [UserRating](docs/UserRating.md)
 - [UserRatingListResponse](docs/UserRatingListResponse.md)
 - [UserRatingSummaryResponse](docs/UserRatingSummaryResponse.md)
 - [Validation](docs/Validation.md)
 - [ValidationError](docs/ValidationError.md)
 - [VariantSet](docs/VariantSet.md)
 - [VariantSetOffer](docs/VariantSetOffer.md)
 - [VariantSetParameter](docs/VariantSetParameter.md)
 - [VariantSets](docs/VariantSets.md)
 - [VariantSetsVariantSet](docs/VariantSetsVariantSet.md)
 - [WarrantiesListWarrantyBasic](docs/WarrantiesListWarrantyBasic.md)
 - [WarrantyBasic](docs/WarrantyBasic.md)
 - [WrapperTypeForPreviewConditions](docs/WrapperTypeForPreviewConditions.md)
 - [WrapsListingAndCommissionsFees](docs/WrapsListingAndCommissionsFees.md)


## Documentation For Authorization


## bearer-token-for-application

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A

## bearer-token-for-user

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://allegro.pl/auth/oauth/authorize
- **Scopes**: N/A


## Author




