from .rest import RestClient


class Organizations(object):
    """Auth0 organizations endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, id=None):
        url = 'https://{}/api/v2/organizations'.format(self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all_organizations(self, page=None, per_page=None):
        """Retrieves a list of all the organizations.

        Args:
           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Clients/get_clients
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(), params=params)

    def get_organization_by_name(self, name=None):
        """Retrieves an organization given its name.

        Args:
           name (str): The name of the organization to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Clients/get_clients
        """
        params = {}
        params['name'] = name

        return self.client.get(self._url(), params=params)

    def create_organization(self, body):
        """Create a new organization.

        Args:
           body (dict): Attributes for the new organization.

        See: https://auth0.com/docs/api/v2#!/Clients/post_clients
        """

        return self.client.post(self._url(), data=body)
    
    def update_organization(self, id, body):
        """Modifies an organization.

        Args:
           id (str): the ID of the organization.

           body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Clients/patch_clients_by_id
        """

        return self.client.patch(self._url(id), data=body)

    def delete_organization(self, id):
        """Deletes an organization and all its related assets.

        Args:
           id (str): Id of organization to delete.

        See: https://auth0.com/docs/api/management/v2#!/Clients/delete_clients_by_id
        """

        return self.client.delete(self._url(id))