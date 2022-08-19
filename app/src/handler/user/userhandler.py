"""
"""
import src.handler.handler as BaseHandler


class UserHandler(BaseHandler.BaseHandler):
    """
    """
    def get_userProperties(self, username, client, *args):
        """Returns the properties of specified user"""
        for list in self._handlerContext:
            try:
                userContext = self._handlerContext[list][client][username]
            except KeyError:
                print("USERHANDLER: %s not listed in %s" %(username, list))
                continue
            if userContext and args:
                userProperties = {}
                for arg in args:
                    try:
                        userProperty = userContext[arg]
                    except KeyError:
                        print("USERHANDLER: %s holds no category called \"%s\"" %(username, arg))
                        continue
                    userProperties.update({arg : userProperty})
                return userProperties
            else:
                return userContext


    def set_userProperty(self, username, category, property):
        """Sets property of specified user"""