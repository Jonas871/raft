#
# This module holds misc functions related to the interface of the tool.
#
# Authors: 
#          Nathan Hamiel
#          Gregory Fleischer
#
# Copyright (c) 2011 RAFT Team
#
# This file is part of RAFT.
#
# RAFT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# RAFT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RAFT.  If not, see <http://www.gnu.org/licenses/>.
#

from core.database.constants import ResponsesTable

def format_headers_str(data):
    """ Format header values from a Python dictionary to a string """
    formatted = ""
    for key in data:
        formatted += "{0}: {1}\n".format(key, data[key])
        
    return(formatted.rstrip())
        
def index_to_id(dataModel, index):
    index = dataModel.index(index.row(), ResponsesTable.ID)
    if index.isValid():
        currentItem = dataModel.data(index)
        if int == type(currentItem):
            return currentItem
        elif currentItem.isValid(): #TODO: remove this code
            print(('FIXME', type(currentItem), 'currentItem', currentItem))
            Id = str(currentItem.toString())
            return Id
    return None

def index_to_url(dataModel, index):
    index = dataModel.index(index.row(), ResponsesTable.URL)
    if index.isValid():
        currentItem = dataModel.data(index)
        if str == type(currentItem):
            return currentItem
        elif currentItem.isValid(): #TODO: remove this code
            print(('FIXME', type(currentItem), 'currentItem', currentItem))
            url = str(currentItem.toString())
            return url
    return None

