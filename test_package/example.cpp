// Including 'hpx/hpx_main.hpp' instead of the usual 'hpx/hpx_init.hpp' enables
// to use the plain C-main below as the direct main HPX entry point.
#include <hpx/hpx_main.hpp>
#include <hpx/include/actions.hpp>
#include <hpx/include/components.hpp>
#include <hpx/include/iostreams.hpp>
#include <hpx/include/lcos.hpp>
#include <hpx/include/util.hpp>

#include <cstddef>
#include <list>
#include <mutex>
#include <set>
#include <vector>

int main()
{
    // Get a list of all available localities.
    std::vector<hpx::naming::id_type> localities =
        hpx::find_all_localities();
    std::size_t const os_threads = hpx::get_os_thread_count();

    std::cout << "Running hpx in " << localities.size() << " locality(ies) and current locality has " << os_threads << " threads." << std::endl;

    return 0;
}
//]
